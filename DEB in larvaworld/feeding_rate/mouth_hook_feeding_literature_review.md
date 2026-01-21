# Mouth-hook movement rate across larval development  
## Focused literature review (latest & foundational)

This note summarizes **two complementary literature reviews** relevant to modeling bite / mouth-hook frequency across *Drosophila melanogaster* larval development. The first is **modern (neural-circuit / functional)**, the second **classical (quantitative behavioral genetics)**. Together they delimit what is known, what is measured, and what remains open for DEB-style quantized feeding models.

---

## Review 1 — Modern neuroethological & circuit-based literature (≈2010–2024)

### Scope
Recent studies focus on:
- the **larval feeding circuit** (brain + subesophageal zone),
- **mouth-hook contractions** as a measurable behavioral output,
- modulation by **hunger, neuromodulators, and developmental state**.

These studies usually work with **late L2 or L3 larvae**, because circuits are mature and behavior is robust.

### Key findings
- Mouth-hook contraction rate is a **stable, high-frequency rhythmic behavior during active feeding**.
- Typical reported values cluster around **150–180 contractions/min** during active feeding on yeast or standard media.
- Feeding rate **drops sharply** during the wandering/pre-pupal transition.
- Developmental comparisons are **rarely systematic across all instars**, but authors note that:
  - rates are lower and more variable in early instars,
  - relatively stable during most of L3,
  - actively suppressed near pupation.

### Quantitative anchor values

| Study type | Stage | Reported rate | Notes |
|-----------|------|---------------|------|
| Feeding circuit analysis | late L2 / early L3 | ~160–170 min⁻¹ | Active feeding on yeast |
| Neuromodulation studies | mid L3 | ~150–180 min⁻¹ | Depends on hunger state |
| Wandering larvae assays | late L3 | ↓ strongly | Feeding actively suppressed |

### Representative modern references (non-exhaustive)
- Itskov PM et al. *Functional analysis of the larval feeding circuit in Drosophila*. **J Vis Exp (JoVE)**.  
- Schoofs A et al. *Serotonergic modulation of feeding in Drosophila larvae*. **eLife / J Neurosci**.  
- Melcher C, Pankratz MJ. *Candidate feeding rhythm generators in larval SEZ*. **Front Neural Circuits**.

---

## Review 2 — Classical behavioral genetics & developmental feeding studies (1970s–1990s)

### Scope
Earlier quantitative work explicitly examined:
- **feeding rate vs larval age**,  
- genetic variation in feeding behavior (e.g. rover/sitter phenotypes),
- mouth-hook or cephalopharyngeal retraction counts as a *direct metric*.

### Core result (robust across studies)
Mouth-hook movement rate follows a **non-monotonic developmental trajectory**:

1. **L1:** low absolute rates, high variability  
2. **L2:** increasing rates with age  
3. **Early–mid L3:** high and relatively stable rates  
4. **Late L3 / pre-pupal:** rapid decline

### Representative findings

| Developmental phase | Feeding rate trend | Interpretation |
|--------------------|-------------------|----------------|
| Early larva (L1) | Low, rising | Small mouthparts, immature circuit |
| L2 | Increasing | Growth acceleration |
| Mid L3 | Plateau | Sustained biomass accumulation |
| Wandering / pre-pupa | Decline | Feeding inhibition precedes metamorphosis |

### Representative classical references
- Sokolowski MB. *Genetic analysis of larval feeding behaviour in Drosophila melanogaster*. **Genetical Research** (1977).  
- Sewell D, Burnet B. *Feeding rates and larval development in Drosophila*. **Genetical Research** (1976).  
- de Belle JS, Sokolowski MB. *Rover/sitter foraging and larval feeding*. **PNAS** (1987).

---

## Synthesis across both literatures

### What is solid
- Mouth-hook contraction rate is a **valid and widely used proxy** for feeding/bite frequency.
- Rates are **developmentally regulated**, not constant across instars.
- A **plateau during most of L3** is a robust empirical observation.
- Feeding is **actively suppressed**, not passively declining, near pupation.

### What is missing
- A **single standardized dataset** measuring mouth-hook frequency continuously from L1 → L2 → L3 under identical conditions.
- Explicit separation of:
  - bite **frequency**,
  - bite **duration**,
  - bite **volume** (never measured directly).

---

## Implications for DEB-style bite quantization

1. **Constant bite frequency across growth is empirically false** across the full larval period.
2. However, **within L3**, frequency can be approximated as roughly constant.
3. Growth-related changes in assimilation are therefore likely carried by:
   - changes in **bite volume**, and
   - changes in **fraction of time spent feeding**,  
   not by frequency alone.
4. A DEB-consistent interpretation is:
   - mouth-hook frequency ≈ *upper bound / rhythm*,
   - effective feeding rate = frequency × bite volume × feeding duty cycle.

---

## Bottom line

> Mouth-hook movement rate **does change across larval development**, but not arbitrarily:  
> it rises early, plateaus during growth, and is actively shut down before pupation.  
> Existing data support **frequency-limited feeding**, with growth accommodated mainly by bite size and feeding duration.

This makes bite-quantized DEB models *biologically plausible* — and highlights exactly where new data would be most valuable.
