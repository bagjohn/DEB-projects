# Appendix: Chemical potential and glucose absorption in *Kaun et al.* (2007)

<!--
Math rendering for VS Code extension "Markdown PDF":
- Requires workspace setting: "markdown-pdf.enableHtml": true
- Loads MathJax (CDN) to typeset $...$ and $$...$$
-->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$']],
      displayMath: [['$$', '$$']],
      processEscapes: true
    },
    svg: { fontCache: 'global' }
  };
</script>
<script async id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>

This appendix **merges and harmonizes** the content of `chemical_potential.md` and `absorption.md` into a **single DEB-consistent reference document**. It is intended to serve as a **methods/appendix section** for manuscripts, theses, or model documentation.

---

## A1. Conceptual separation (DEB notation)

We distinguish strictly between:

- **Food density** $X$  
  (substrate density, typically in C-mol·cm⁻³)

- **Chemical potential of food** $\mu_X$  
  (energy per C-mol of substrate; J·C-mol⁻¹)

- **Environmental energy density** (derived quantity)

  $$
  \varepsilon_X \equiv \mu_X X \qquad [\varepsilon_X]=\mathrm{J\,cm^{-3}}
  $$

Only $X$ enters the DEB functional response; $\varepsilon_X$ is a convenient derived quantity when diets are specified by mass or molarity.

---

## A2. Diet context for tracer experiments

All ¹⁴C-glucose experiments in *Kaun et al.* (2007) were conducted on:

- **Yeast paste** (2 : 1 water : yeast, w/w)
- with **¹⁴C-labelled glucose added as a tracer**

Thus:
- the **diet is mixed and nutritionally complete**,
- glucose is **not** the sole nutrient,
- the tracer probes **carbohydrate-specific ingestion and retention**, not total feeding or total assimilation.

---

## A3. Chemical potential used

For carbohydrates (glucose / fructose), we adopt:

$$
\mu_{\mathrm{carb}} = 4.68\times10^5\;\mathrm{J\,C\!\!\text{-}mol^{-1}}
$$

This value is consistent with the energetic densities used elsewhere in the diet reconstruction and allows direct translation between tracer uptake (C-mol) and energy (J).

---

## A4. Extracted ¹⁴C-glucose tracer values

### A4.1 Intake (15 min feeding)

| Genotype | Intake (fmol glucose·larva⁻¹) |
|---|---:|
| forᴿ | 600 |
| forˢ | 1200 |
| forˢ² | 1050 |

### A4.2 Absorption (after 3 h chase)

| Genotype | Absorption (fmol glucose·larva⁻¹) |
|---|---:|
| forᴿ | 309.68 |
| forˢ | 193.55 |
| forˢ² | 182.49 |

Values were digitized from Fig. 3B and are reported in the original paper only graphically.

---

## A5. Conversion to C-moles and energy

Constants:
- glucose: $n_C = 6$
- $1\,\mathrm{fmol} = 10^{-15}\,\mathrm{mol}$

For a value $B$ (fmol glucose per larva):

$$
 n_C = 6\,B\times10^{-15}\quad [\mathrm{C\!\!\text{-}mol}]
$$

$$
 E = \mu_{\mathrm{carb}}\, n_C \quad [\mathrm{J}]
$$

| Genotype | Absorption (fmol) | $n_C$ (C-mol·larva⁻¹) | Energy retained (J·larva⁻¹) |
|---|---:|---:|---:|
| forᴿ | 309.68 | $1.86\times10^{-12}$ | $8.70\times10^{-7}$ |
| forˢ | 193.55 | $1.16\times10^{-12}$ | $5.43\times10^{-7}$ |
| forˢ² | 182.49 | $1.09\times10^{-12}$ | $5.12\times10^{-7}$ |

---

## A6. Average fluxes (DEB-style interpretation)

Feeding window:

$$
\Delta t_{\mathrm{feed}} = 15\,\mathrm{min} = 0.0104167\,\mathrm{d}
$$

Average ingestion flux (glucose-derived carbon):

$$
\dot J_X^{(15)} = \frac{n_{C,\mathrm{intake}}}{\Delta t_{\mathrm{feed}}}
$$

Average net absorbed flux:

$$
\dot J_{\mathrm{abs}}^{(15)} = \frac{n_{C,\mathrm{abs}}}{\Delta t_{\mathrm{feed}}}
$$

Corresponding energy flux:

$$
\dot p = \mu_{\mathrm{carb}}\,\dot J
$$

---

## A7. Absorption efficiency proxy

A robust, dimensionless quantity is:

$$
\boxed{\eta_{\mathrm{abs}} = \frac{\text{Absorption}}{\text{Intake}}}
$$

| Genotype | $\eta_{\mathrm{abs}}$ |
|---|---:|
| forᴿ | 0.516 |
| forˢ | 0.161 |
| forˢ² | 0.174 |

This quantity captures **post-ingestive carbohydrate retention efficiency** and can be used in DEB-inspired models as a **genotype-specific modifier of effective assimilation for carbohydrates**, without reinterpreting it as total reserve assimilation.

---

## A8. DEB-consistent placement

- Diet context: high food density → $f\approx1$
- Tracer informs **pathway-specific processing**, not overall feeding capacity
- Constrains **relative differences**, not absolute $\dot p_{Am}$ or $K$

---

**End of appendix**

