"""
Parse a DEB parameter table from a single HTML file and write JSON output.

Expected HTML structure (minimum required):
1) A <title> element containing the species name (used for metadata["species"]).
   Example: <title>Drosophila_melanogaster</title>

2) A parameter table with columns:
   symbol | unit | value | free | description
   The default table is identified by id="par" (as in <table id="par">).

3) A data & predictions table with columns:
   data | prd | RE | symbol | units | description
   The default table is identified by id="prd" (as in <table id="prd">).

3) A header like "abp parameters at 20.0 degC" in an <h2> element.
   The leading token (e.g., "abp") becomes metadata["typified_model"].

Behavior notes:
- If id="par" is not found, the script will fall back to the first table.
- Each parameter row must contain at least 5 cells; extra columns are ignored.
- "value" is parsed as float when possible, otherwise left as text.
- "free" is coerced to boolean-like integer 0 or 1 (non-zero -> 1).

Output format:
{
  "metadata": {"species": "...", "typified_model": "..."},
  "parameters": [
    {"symbol": "...", "unit": "...", "value": ..., "free": 0/1, "description": "..."},
    ...
  ],
  "data_predictions": [
    {"data": ..., "prd": ..., "RE": ..., "symbol": "...", "unit": "...", "description": "..."},
    ...
  ]
}

Default output path:
<script_folder>/<species>_DEB_pars.json

Usage example (run from the script folder):
py .\retrieve_pars_from_html_to_json.py ^
  "..\Drosophilla_DEB_Evridiki\Drosophila_melanogaster_res.html" ^
  --out ".\Drosophila_melanogaster_DEB_pars.json"
"""

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Dict, Optional, Any


class ParameterTableParser(HTMLParser):
    """Parse rows from a specific HTML table (default: id='par')."""

    def __init__(self, table_id: Optional[str] = "par") -> None:
        super().__init__()
        self.table_id = table_id
        self._in_table = False
        self._in_tr = False
        self._in_cell = False
        self._cell_chunks: List[str] = []
        self._current_row: List[str] = []
        self.rows: List[List[str]] = []

    def handle_starttag(self, tag: str, attrs: List[tuple[str, Optional[str]]]) -> None:
        if tag.lower() == "table":
            attr_dict = {k.lower(): (v or "") for k, v in attrs}
            if self.table_id is None or attr_dict.get("id") == self.table_id:
                self._in_table = True
        if self._in_table and tag.lower() == "tr":
            self._in_tr = True
            self._current_row = []
        if self._in_table and self._in_tr and tag.lower() in ("td", "th"):
            self._in_cell = True
            self._cell_chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_cell:
            self._cell_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._in_table and self._in_tr and tag.lower() in ("td", "th"):
            self._in_cell = False
            cell_text = "".join(self._cell_chunks).strip()
            self._current_row.append(cell_text)
            self._cell_chunks = []
        if self._in_table and tag.lower() == "tr":
            self._in_tr = False
            if self._current_row:
                self.rows.append(self._current_row)
                self._current_row = []
        if self._in_table and tag.lower() == "table":
            self._in_table = False


class MetadataParser(HTMLParser):
    """Extract species (from <title>) and typified model (from <h2> header)."""

    def __init__(self) -> None:
        super().__init__()
        self._in_title = False
        self._in_h2 = False
        self._title_chunks: List[str] = []
        self._h2_chunks: List[str] = []
        self.species: Optional[str] = None
        self.typified_model: Optional[str] = None

    def handle_starttag(self, tag: str, attrs: List[tuple[str, Optional[str]]]) -> None:
        if tag.lower() == "title":
            self._in_title = True
            self._title_chunks = []
        elif tag.lower() == "h2":
            self._in_h2 = True
            self._h2_chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_chunks.append(data)
        elif self._in_h2:
            self._h2_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False
            title = "".join(self._title_chunks).strip()
            if title:
                self.species = title
        elif tag.lower() == "h2":
            self._in_h2 = False
            h2_text = "".join(self._h2_chunks).strip()
            if h2_text and "parameters at" in h2_text.lower():
                token = h2_text.split()[0]
                if token:
                    self.typified_model = token


def _coerce_value(text: str) -> Any:
    """Parse numeric text into float when possible, otherwise return raw text."""

    t = text.strip()
    if t == "":
        return None
    try:
        return float(t)
    except ValueError:
        try:
            return float(t.replace(" ", ""))
        except Exception:
            return t


def _coerce_free(text: str) -> Optional[int]:
    """Convert 'free' to boolean-like integer (0 or 1)."""

    val = _coerce_value(text)
    if val is None:
        return None
    try:
        return 1 if float(val) != 0 else 0
    except Exception:
        return None


def _rows_to_params(rows: List[List[str]]) -> List[Dict[str, Any]]:
    """Convert parsed rows to a list of parameter dictionaries."""

    params: List[Dict[str, Any]] = []
    for row in rows:
        if not row:
            continue
        if row[0].strip().lower() == "symbol":
            continue
        if len(row) < 5:
            continue
        symbol = row[0].strip()
        unit = row[1].strip()
        value = _coerce_value(row[2])
        free = _coerce_free(row[3])
        description = row[4].strip()
        params.append(
            {
                "symbol": symbol,
                "unit": unit,
                "value": value,
                "free": free,
                "description": description,
            }
        )
    return params


def _rows_to_data_predictions(rows: List[List[str]]) -> List[Dict[str, Any]]:
    """Convert parsed rows to a list of data/prediction dictionaries."""

    items: List[Dict[str, Any]] = []
    for row in rows:
        if not row:
            continue
        if row[0].strip().lower() == "data":
            continue
        if len(row) < 4:
            continue

        data_text = row[0].strip() if len(row) >= 1 else ""
        prd_text = row[1].strip() if len(row) >= 2 else ""
        re_text = row[2].strip() if len(row) >= 3 else ""
        symbol = row[3].strip() if len(row) >= 4 else ""
        unit_text = row[4].strip() if len(row) >= 5 else ""
        description = row[5].strip() if len(row) >= 6 else ""

        # Handle rows with colspan that reduce the cell count
        if len(row) == 4:
            # data/prd are merged, units/description are merged into the last cell
            data_text = row[0].strip()
            prd_text = ""
            re_text = row[1].strip()
            symbol = row[2].strip()
            unit_text = ""
            description = row[3].strip()
        elif len(row) == 5:
            # Assume missing unit (units+description merged)
            description = row[4].strip()
            unit_text = ""

        items.append(
            {
                "data": _coerce_value(data_text),
                "prd": _coerce_value(prd_text) if prd_text != "" else None,
                "RE": _coerce_value(re_text),
                "symbol": symbol,
                "unit": unit_text,
                "description": description,
            }
        )

    return items


def retrieve_pars_from_html(
    html_path: str, table_id: Optional[str] = "par"
) -> Dict[str, Any]:
    """
    Parse the HTML file and return metadata + parameters + data predictions.

    Returns a dict with keys:
    - metadata: {species, typified_model}
    - parameters: list of parameter dicts
    - data_predictions: list of data/prediction dicts
    """

    path = Path(html_path)
    html_text = path.read_text(encoding="utf-8", errors="replace")

    metadata_parser = MetadataParser()
    metadata_parser.feed(html_text)

    par_parser = ParameterTableParser(table_id=table_id)
    par_parser.feed(html_text)
    par_rows = par_parser.rows

    if not par_rows and table_id is not None:
        par_parser = ParameterTableParser(table_id=None)
        par_parser.feed(html_text)
        par_rows = par_parser.rows

    prd_parser = ParameterTableParser(table_id="prd")
    prd_parser.feed(html_text)
    prd_rows = prd_parser.rows

    metadata = {
        "species": metadata_parser.species,
        "typified_model": metadata_parser.typified_model,
    }

    return {
        "metadata": metadata,
        "parameters": _rows_to_params(par_rows),
        "data_predictions": _rows_to_data_predictions(prd_rows),
    }


def _sanitize_species_for_filename(species: str) -> str:
    """Create a safe filename token from species while preserving readability."""

    cleaned = species.strip()
    if not cleaned:
        return ""
    cleaned = cleaned.replace("/", "_").replace("\\", "_")
    return cleaned


def main() -> int:
    """CLI entrypoint."""

    ap = argparse.ArgumentParser(description="Parse DEB parameter table from an HTML results file.")
    ap.add_argument("html_path", help="Path to the *_res.html file")
    ap.add_argument("--table-id", default="par", help="HTML table id to parse (default: par)")
    ap.add_argument(
        "--out",
        help="Output JSON path. Defaults to <html_stem>_pars.json in the same folder.",
    )
    args = ap.parse_args()

    payload = retrieve_pars_from_html(args.html_path, table_id=args.table_id)

    html_path = Path(args.html_path)
    default_out_dir = Path(__file__).resolve().parent
    species = payload.get("metadata", {}).get("species")
    if args.out:
        out_path = Path(args.out)
    else:
        if not species:
            raise ValueError("Could not determine species from <title> in the HTML file.")
        safe_species = _sanitize_species_for_filename(str(species))
        out_path = default_out_dir / f"{safe_species}_DEB_pars.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
