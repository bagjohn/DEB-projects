# Tutorial: Extracting Dietary Recipes and Expressing Them in DEB Form (Kaun 2007 Example)

This walkthrough shows how to go from a paper’s diet recipe (masses or molarities) to DEB-ready food inputs. We use Kaun et al. (2007) as the worked example.

## 1) Collect the recipe

- Transcribe each ingredient with amount **per liter** (or per batch, then normalize to 1 L).
- Tag each as **edible** (contributes energy) or **inert** (agar/gelling agents, preservatives, salts).
- Example (Kaun standard medium, per L): yeast 50 g, sucrose 100 g, agar 16 g, minerals (trace), water to 1 L.

## 2) Normalize and separate edible components

- Convert amounts to **mass concentrations** \(\rho_i\) in g·cm\(^{-3}\): \(\rho_i = \text{grams per liter} / 1000\).
- Keep only edible ingredients for energy calculations; retain inerts for documentation only.

## 3) Assign per-mass energy content

- Use literature or standard food-energy values (J·g\(^{-1}\)) for each edible component, call them \(e_i\).
- Example values (as used in Kaun2007 note):
  - Yeast: \(e_Y \approx 21 \times 10^3\) J·g\(^{-1}\)
  - Sucrose (or glucose/fructose): \(e_S \approx 16.5 \times 10^3\) J·g\(^{-1}\)

## 4) Compute energy per volume (environmental energy density)

For a recipe with edible components \(i\):
\[
\varepsilon_X = \sum_i \rho_i\, e_i \qquad [\varepsilon_X] = \text{J·cm}^{-3}.
\]
This is the DEB-relevant food energy density (often denoted \(\Phi_X\) or \(\varepsilon_X\)).

### Kaun standard medium (worked numbers)
- \(\rho_Y = 50/1000 = 0.050\) g·cm\(^{-3}\)
- \(\rho_S = 100/1000 = 0.100\) g·cm\(^{-3}\)
- \(\varepsilon_X = 0.050\times21\times10^3 + 0.100\times16.5\times10^3 \approx 2.7\times10^3\) J·cm\(^{-3}\)
- Dilutions: for quality factor \(q\), \(\varepsilon_X(q) = q\,\varepsilon_X\).

### Kaun yeast paste (2:1 water:yeast w/w)
- Yeast mass fraction \(w_Y = 1/3\); paste density \(\approx 1\) g·cm\(^{-3}\) → \(\rho_Y \approx 0.333\) g·cm\(^{-3}\)
- \(\varepsilon_X \approx 0.333\times21\times10^3 \approx 7.0\times10^3\) J·cm\(^{-3}\)

### Kaun glucose–agarose (10% w/v)
- \(\rho_G = 0.10\) g·cm\(^{-3}\); \(e_G \approx 15.6\times10^3\) J·g\(^{-1}\)
- \(\varepsilon_X \approx 1.56\times10^3\) J·cm\(^{-3}\)

### Kaun fructose–agarose (2 mol·L\(^{-1}\))
- Molar mass 180 g·mol\(^{-1}\); \(\rho_F = 2\times180/1000 = 0.36\) g·cm\(^{-3}\)
- \(\varepsilon_X \approx 0.36\times15.6\times10^3 \approx 5.6\times10^3\) J·cm\(^{-3}\)

## 5) (Optional) Map to DEB food density \(X\) and chemical potential \(\mu_X\)

If your DEB implementation expects \(X\) in C-mol·cm\(^{-3}\) and a chemical potential \(\mu_X\) in J·C-mol\(^{-1}\):
- Choose or estimate \(\mu_X\) (food quality).
- Recover \(X\) from \(\varepsilon_X = \mu_X X\) ⇒ \(X = \varepsilon_X / \mu_X\).
- Keep \(\mu_X\) consistent across foods when comparing only density changes; vary \(\mu_X\) if food quality differs.

## 6) Document assumptions explicitly

- Densities (often assume 1 g·cm\(^{-3}\) for gels/slurries unless reported).
- Energy contents \(e_i\) sources.
- Which ingredients are counted as edible vs. inert.
- Any dilution/quality factors applied (e.g., 25%, 15%).

## 7) Slot into the DEB equations

Use \(\varepsilon_X\) (or \(X\) and \(\mu_X\)) in the functional response and assimilation chain:
\[
\varepsilon_X = \mu_X X, \qquad f = \frac{X}{K+X} = \frac{\varepsilon_X}{\varepsilon_K + \varepsilon_X}, \quad \varepsilon_K \equiv \mu_X K.
\]
Assimilation for V1-morphs (volume-proportional uptake):
\[
\dot p_A = f\,\{\dot p_{Am}\} V.
\]
Feeding motions (from `feeding_rate_in_DEB.md`):
\[
f_{\text{feed}}(\Phi_X) = \frac{\{\dot{p}_{Am}\}\,\{\dot{F}_m\}}{\{\dot{p}_{Am}\} + \kappa_{\text{bite}}\,\kappa_X\,\{\dot{F}_m\}\,\Phi_X}, \quad \Phi_X \equiv \varepsilon_X.
\]

## 8) Minimal checklist for new papers

1. Transcribe recipe to g·L\(^{-1}\) (or mol·L\(^{-1}\) → g·L\(^{-1}\)).
2. Mark edible vs. inert; convert to \(\rho_i\) (g·cm\(^{-3}\)).
3. Assign \(e_i\) (J·g\(^{-1}\)).
4. Compute \(\varepsilon_X = \sum \rho_i e_i\).
5. (Optional) Derive \(X = \varepsilon_X / \mu_X\) if DEB model needs \(X\) explicitly.
6. Record assumptions and any dilution factor \(q\).

## 9) Why this works

Papers give foods in kitchen units (g, %, molarity). DEB needs **energy per volume** (or equivalently \(X\) and \(\mu_X\)). The conversion above is linear and transparent, making recipes portable across experiments and simulators.

---

*File: recipy_extraction_tutorial.md — based on Kaun et al. (2007) diets and the DEB feeding-rate formulation in `feeding_rate_in_DEB.md`.*
