# Tutorial: Extracting Diet Recipes and Converting to DEB Inputs (Kaun 2007 Worked Example)

This tutorial starts by defining and computing the **chemical potential of food** \(\mu_X\) (J·C-mol\(^{-1}\)) for each recipe, then derives the DEB food density \(X\) (C-mol·cm\(^{-3}\)) and the energy density \(\varepsilon_X = \mu_X X\) (J·cm\(^{-3}\)). All numbers use the Kaun et al. (2007) diets as concrete examples.

## 0. Assumptions and constants (with provenance)
- **Energy per gram (gross energy)**: taken from standard food-energy values (e.g., bomb-calorimetry or nutrition tables). Here
  \[
  e_Y = 21{,}000\,\mathrm{J\,g^{-1}},\qquad e_S = 15{,}600\,\mathrm{J\,g^{-1}},
  \]
  with \(e_Y\) for yeast (mixed macronutrients) and \(e_S\) for sucrose/glucose/fructose as carbohydrate proxies.
- **Molar mass and carbon mass per C-mol (DEB notation)**: For C\(_{n_C}\)H\(_{n_H}\)O\(_{n_O}\)N\(_{n_N}\),
  \[
  w = 12 n_C + 1 n_H + 16 n_O + 14 n_N\,\,\mathrm{g\,mol^{-1}},\qquad
  w_C = \frac{w}{n_C}\,\,\mathrm{g\,C\text{-}mol^{-1}}.
  \]
- **Chemical potential**: DEB defines the chemical potential of an ingredient as its energy per C-mol,
  \[
  \mu_{X,i} = e_i\,w_{C,i}\,\,\mathrm{J\,C\text{-}mol^{-1}},
  \]
  and for a mixture \(\mu_X = \varepsilon_X/X\) with \(\varepsilon_X = \sum \rho_i e_i\) and \(X = \sum \rho_i/w_{C,i}\) (food eqs. in DEB textbook, Ch. 4).

Stoichiometry and derived \(w_C\), \(\mu_{X,i}\):

| Compound | Empirical formula | \(n_C\) | \(n_H\) | \(n_O\) | \(n_N\) | \(w_C = w/n_C\) (g·C-mol\(^{-1}\)) | \(\mu_{X,i}=e_i w_C\) (J·C-mol\(^{-1}\)) |
|---|---|---:|---:|---:|---:|---:|---:|
| Yeast (biomass proxy) | C\(_1\)H\(_{1.8}\)O\(_{0.5}\)N\(_{0.2}\) | 1 | 1.8 | 0.5 | 0.2 | 24.63 | 5.17×10<sup>5</sup> |
| Sucrose | C\(_{12}\)H\(_{22}\)O\(_{11}\) | 12 | 22 | 11 | 0 | 28.52 | 4.45×10<sup>5</sup> |
| Glucose / Fructose | C\(_6\)H\(_{12}\)O\(_6\) | 6 | 12 | 6 | 0 | 30.03 | 4.68×10<sup>5</sup> |
- Only edible ingredients (yeast, sugars) contribute to \(X\), \(\mu_X\), and \(\varepsilon_X\); agar/minerals/preservatives are inert for energy.

## 1. Formulas (compute \(\mu_X\) first, then \(X\))
- **Bulk density** of gels/pastes \(\rho_{\text{bulk}}\): assume \(\approx 1\,\mathrm{g\,cm^{-3}}\) unless measured; for a batch with mass \(m\) (g) filling volume \(V\) (cm\(^3\)), \(\rho_{\text{bulk}} = m/V\). Use \(\rho_i = m_i/V\) to get each ingredient’s mass concentration.

For each edible ingredient \(i\):
- Mass concentration: \(\rho_i\) (g·cm\(^{-3}\))
- Energy per mass: \(e_i\) (J·g\(^{-1}\))
- Carbon mass per C-mol: \(w_{C,i}\) (g·C-mol\(^{-1}\))

Derived totals for the recipe:
\[
\varepsilon_X = \sum_i \rho_i e_i \quad [\mathrm{J\,cm^{-3}}],\qquad
X = \sum_i \frac{\rho_i}{w_{C,i}} \quad [\mathrm{C\text{-}mol\,cm^{-3}}],\qquad
\mu_X = \frac{\varepsilon_X}{X} \quad [\mathrm{J\,C\text{-}mol^{-1}}].
\]
(If a DEB model already fixes \(\mu_X\), you can instead set \(\mu_X\) and compute \(X = \varepsilon_X/\mu_X\).)

## 2. Ingredient inputs (Kaun 2007)
| Ingredient | Recipe mass per L (g) | \(\rho_i\) (g·cm\(^{-3}\)) | \(e_i\) (J·g\(^{-1}\)) | \(w_{C,i}\) (g·C-mol\(^{-1}\)) | \(\mu_{X,i}=e_i\,w_{C,i}\) (J·C-mol\(^{-1}\)) |
|---|---:|---:|---:|---:|---:|
| Yeast | 50 | 0.050 | 21,000 | 24.63 | 5.17×10<sup>5</sup> |
| Sucrose | 100 | 0.100 | 15,600 | 28.52 | 4.45×10<sup>5</sup> |
| Agar (inert) | 16 | 0.016 | — | — | — |
| Yeast paste (mass fraction 1/3) | — | 0.333 | 21,000 | 24.63 | 5.17×10<sup>5</sup> |
| Glucose (10% w/v) | 100 | 0.100 | 15,600 | 30.03 | 4.68×10<sup>5</sup> |
| Fructose (2 M) | 360 | 0.360 | 15,600 | 30.03 | 4.68×10<sup>5</sup> |

## 3. Worked results (Kaun diets)
| Diet | Edible \(\rho_i\) (g·cm\(^{-3}\)) | \(\varepsilon_X\) (J·cm\(^{-3}\)) | \(X\) (C-mol·cm\(^{-3}\)) | \(\mu_X\) (J·C-mol\(^{-1}\)) |
|---|---|---:|---:|---:|
| Standard medium (yeast 50 g/L, sucrose 100 g/L) | \(\rho_Y=0.050\), \(\rho_S=0.100\) | 2.70×10<sup>3</sup> | 5.54×10<sup>-3</sup> | 4.88×10<sup>5</sup> |
| Standard (quality \(q\)) | scaled by \(q\) | \(q\,2.70×10^3\) | \(q\,5.54×10^{-3}\) | 4.88×10<sup>5</sup> |
| Yeast paste (2:1 water:yeast) | \(\rho_Y\approx0.333\) | 6.99×10<sup>3</sup> | 1.35×10<sup>-2</sup> | 5.17×10<sup>5</sup> |
| Glucose–agarose (10% w/v) | \(\rho_G=0.100\) | 1.56×10<sup>3</sup> | 3.33×10<sup>-3</sup> | 4.68×10<sup>5</sup> |
| Fructose–agarose (2 M) | \(\rho_F=0.360\) | 5.62×10<sup>3</sup> | 1.20×10<sup>-2</sup> | 4.69×10<sup>5</sup> |

Notes on the calculations:
- \(\varepsilon_X\) uses \(\varepsilon_X = \sum \rho_i e_i\).
- \(X\) uses \(\rho_i / w_{C,i}\) summed over edible ingredients.
- \(\mu_X\) is the ratio \(\varepsilon_X / X\); it stays constant under uniform dilution (\(q\)) because both numerator and denominator scale by \(q\).

## 4. Quick recipe-to-DEB checklist
1) Transcribe ingredient masses; convert to \(\rho_i\) (g·cm\(^{-3}\)).
2) Mark edible vs. inert.
3) Assign \(e_i\) and \(w_{C,i}\).
4) Compute \(\varepsilon_X\), then \(X\), then \(\mu_X = \varepsilon_X/X\).
5) For dilutions, multiply \(\rho_i\) by \(q\); \(\mu_X\) stays the same.

## 5. Slotting into DEB equations
- Energy density: \(\Phi_X \equiv \varepsilon_X\).
- Food density: \(X = \varepsilon_X / \mu_X\) (if \(\mu_X\) is fixed), or \(\mu_X = \varepsilon_X/X\) (if both are derived).
- Functional response: \(f = X/(K+X) = \Phi_X/(\Phi_K + \Phi_X)\) with \(\Phi_K = \mu_X K\).
- V1-morph assimilation: \(\dot p_A = f\,\{\dot p_{Am}\} V\).
- Feeding motions (from feeding_rate_in_DEB): \(f_{\text{feed}}(\Phi_X) = \dfrac{\{\dot{p}_{Am}\}\,\{\dot{F}_m\}}{\{\dot{p}_{Am}\} + \kappa_{\text{bite}}\,\kappa_X\,\{\dot{F}_m\}\,\Phi_X}\).

## 6. Takeaways
- Start with \(\mu_X\): it is set by recipe composition via \(\mu_X = \varepsilon_X/X\).
- \(\varepsilon_X\) scales linearly with dilution; \(\mu_X\) does not, for uniform dilutions.
- The tables above provide ready-to-use \(\mu_X\), \(X\), and \(\varepsilon_X\) for the Kaun (2007) diets.

---

*File: recipy_extraction_tutorial_2.md — Kaun 2007 diets expressed in DEB terms.*
