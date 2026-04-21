# ¹⁴C‑glucose absorption assay in *Kaun et al.* (2007)

This file consolidates **all details, values, conversions, and DEB‑consistent interpretations** of the short‑term **¹⁴C‑glucose feeding and absorption experiments** in *Kaun et al.* (2007).

---

## 1. Experimental context

### Diet
- **Substrate:** **yeast paste** (2 : 1 water : yeast, w/w)
- The yeast paste was **spiked with ¹⁴C‑labelled glucose**
- Larvae were therefore feeding in a **rich, mixed diet context**; glucose acts **only as a tracer**, not as the sole nutrient source.

### Larval stage
- Late **feeding third‑instar larvae**
- Genotypes: **forᴿ (rover)**, **forˢ (sitter)**, **forˢ²**

### Timing
- **Feeding (intake) window:** 15 min on labelled yeast paste
- **Chase:** 3 h on unlabeled food to clear gut contents

---

## 2. What is measured

Two quantities are reported (graphically) in Fig. 3B of the paper:

1. **Intake**  
   Total ¹⁴C‑glucose present immediately after 15 min feeding

2. **Absorption (retention)**  
   ¹⁴C‑glucose remaining in the larva after a 3 h chase

Units in the figure: **fmol glucose per larva**.

> Importantly, this assay measures **glucose‑specific ingestion and retention**, not total food intake or total assimilation.

---

## 3. Extracted numerical values (digitized from Fig. 3B)

### Intake (15 min)
| Genotype | Intake (fmol glucose·larva⁻¹) |
|---|---:|
| forᴿ | 600 |
| forˢ | 1200 |
| forˢ² | 1050 |

### Absorption (after 3 h chase)
| Genotype | Absorption (fmol glucose·larva⁻¹) |
|---|---:|
| forᴿ | 309.68 |
| forˢ | 193.55 |
| forˢ² | 182.49 |

These values are **not tabulated in the paper** and were obtained by digitizing the plotted bar heights.

---

## 4. Constants and unit conversions (DEB‑consistent)

- Glucose formula: \(\mathrm{C_6H_{12}O_6}\)
- Carbon atoms per molecule: \(n_C = 6\)
- \(1\,\mathrm{fmol} = 10^{-15}\,\mathrm{mol}\)

### Time windows
- Feeding window:  
  \[\Delta t_{\mathrm{feed}} = 15\,\mathrm{min} = 0.0104167\,\mathrm{d}\]
- Chase window:  
  \[\Delta t_{\mathrm{chase}} = 3\,\mathrm{h} = 0.125\,\mathrm{d}\]

### Chemical potential (as used elsewhere in this project)
\[
\mu_{\mathrm{glc}} = 4.68\times10^{5}\,\mathrm{J\,C\!\!\text{-}mol^{-1}}
\]

---

## 5. Amounts converted to C‑moles and energy

For a value \(B\) in fmol glucose per larva:
\[
 n_{\mathrm{glc}} = B\times10^{-15}\,\mathrm{mol}
\]
\[
 n_C = 6\,n_{\mathrm{glc}}\quad [\mathrm{C\!\!\text{-}mol}]
\]
\[
 E_{\mathrm{abs}} = \mu_{\mathrm{glc}}\,n_C\quad [\mathrm{J}]
\]

| Genotype | Absorption (fmol) | \(n_C\) (C‑mol·larva⁻¹) | \(E_{\mathrm{abs}}\) (J·larva⁻¹) |
|---|---:|---:|---:|
| forᴿ | 309.68 | \(1.858\times10^{-12}\) | \(8.70\times10^{-7}\) |
| forˢ | 193.55 | \(1.161\times10^{-12}\) | \(5.43\times10^{-7}\) |
| forˢ² | 182.49 | \(1.095\times10^{-12}\) | \(5.12\times10^{-7}\) |

---

## 6. Average DEB‑style fluxes (optional)

### 6.1 Average ingestion flux during feeding (15 min)
\[
\dot J_X^{(15)} = \frac{n_{C,\mathrm{intake}}}{\Delta t_{\mathrm{feed}}}
\quad [\mathrm{C\!\!\text{-}mol\,d^{-1}}]
\]

### 6.2 Average net absorbed flux (referenced to feeding window)
\[
\dot J_{\mathrm{abs}}^{(15)} = \frac{n_{C,\mathrm{abs}}}{\Delta t_{\mathrm{feed}}}
\]

Energy flux:
\[
\dot p = \mu_{\mathrm{glc}}\,\dot J
\]

| Genotype | \(\dot J_X^{(15)}\) (C‑mol·d⁻¹) | \(\dot p_X^{(15)}\) (J·d⁻¹) | \(\dot J_{\mathrm{abs}}^{(15)}\) (C‑mol·d⁻¹) | \(\dot p_{\mathrm{abs}}^{(15)}\) (J·d⁻¹) |
|---|---:|---:|---:|---:|
| forᴿ | \(3.46\times10^{-10}\) | \(1.62\times10^{-4}\) | \(1.78\times10^{-10}\) | \(8.35\times10^{-5}\) |
| forˢ | \(6.91\times10^{-10}\) | \(3.23\times10^{-4}\) | \(1.11\times10^{-10}\) | \(5.22\times10^{-5}\) |
| forˢ² | \(6.05\times10^{-10}\) | \(2.83\times10^{-4}\) | \(1.05\times10^{-10}\) | \(4.92\times10^{-5}\) |

---

## 7. Absorption / intake fraction

A dimensionless and robust quantity is the **absorption fraction**:
\[
\boxed{\eta_{\mathrm{abs}} = \frac{\text{Absorption}}{\text{Intake}}}
\]

| Genotype | \(\eta_{\mathrm{abs}}\) |
|---|---:|
| forᴿ | 0.516 |
| forˢ | 0.161 |
| forˢ² | 0.174 |

This fraction captures **post‑ingestive processing efficiency** for glucose‑derived carbon.

### A5. Window-aware alternative assimilation efficiency (rate/flux based)

To explicitly account for the different measurement windows, convert absolute amounts first to average fluxes:

Feeding-window intake flux:
\[
\dot J_{X,\mathrm{feed}} = \frac{n_{C,\mathrm{intake}}}{\Delta t_{\mathrm{feed}}}
\]

Chase-window retained/absorbed flux:
\[
\dot J_{A,\mathrm{chase}} = \frac{n_{C,\mathrm{abs}}}{\Delta t_{\mathrm{chase}}}
\]

Define the alternative window-aware coefficient as the flux ratio:
\[
\boxed{\eta_{\mathrm{win}} = \frac{\dot J_{A,\mathrm{chase}}}{\dot J_{X,\mathrm{feed}}}}
= \frac{n_{C,\mathrm{abs}}/\Delta t_{\mathrm{chase}}}{n_{C,\mathrm{intake}}/\Delta t_{\mathrm{feed}}}
= \eta_{\mathrm{abs}}\,\frac{\Delta t_{\mathrm{feed}}}{\Delta t_{\mathrm{chase}}}
\]

Using:
\[
\Delta t_{\mathrm{feed}}=0.0104167\,\mathrm{d},\qquad
\Delta t_{\mathrm{chase}}=0.125\,\mathrm{d}
\]
gives:
\[
\frac{\Delta t_{\mathrm{feed}}}{\Delta t_{\mathrm{chase}}}=0.0833336
\]

Therefore:

| Genotype | \(\dot J_{X,\mathrm{feed}}\) (C-mol·d⁻¹) | \(\dot J_{A,\mathrm{chase}}\) (C-mol·d⁻¹) | \(\eta_{\mathrm{win}}\) |
|---|---:|---:|---:|
| forᴿ | \(3.46\times10^{-10}\) | \(1.49\times10^{-11}\) | 0.0430 |
| forˢ | \(6.91\times10^{-10}\) | \(9.29\times10^{-12}\) | 0.0134 |
| forˢ² | \(6.05\times10^{-10}\) | \(8.76\times10^{-12}\) | 0.0145 |

So in this alternative formulation, the coefficient is still dimensionless, but it now explicitly incorporates that intake was measured over a short 15 min feeding window, while retained absorbed label was measured over a longer 3 h chase/absorption window.

---

## 8. DEB‑consistent interpretation

- The assay was performed on **yeast paste** (energetically dominant substrate), while ¹⁴C-glucose is a pathway tracer.
- If tracer mass/volume density is not reported, tracer energy is not introduced as an independent dietary energy input in DEB energetics.
- ¹⁴C‑glucose traces **only carbohydrate pathways**.
- Intake reflects **glucose‑specific ingestion**, not total feeding.
- Absorption reflects **retained glucose‑derived carbon**, downstream of ingestion.

### Correct DEB placement
- Functional response is computed, not assumed:
\[
f=\frac{X}{X+K}
\]
- With project notation:
\[
K = \frac{\{\dot J_{Xm}\}}{\{\dot F_m\}} = \frac{\{\dot p_{Am}\}}{\kappa_X\,\mu_X\,\{\dot F_m\}}
\]
- If maximum ingestion is similar across genotypes, differences in effective assimilation efficiency \(\kappa_X\) imply differences in \(K\).
- These data constrain genotype differences in **post‑ingestive uptake / retention** and are used to define relative effective-assimilation modifiers.
- A DEB‑consistent usage is to treat \(\eta_{\mathrm{abs}}\) as a proxy for a
  carbohydrate‑specific effective assimilation factor:
\[
\kappa_{X,\mathrm{carb}}^{\mathrm{eff}} \propto \eta_{\mathrm{abs}}
\]

This explains why rovers ingest less glucose but retain more of what they ingest.

---

**End of file — absorption.md**

