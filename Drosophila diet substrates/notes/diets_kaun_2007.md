# Diets used in Kaun et al. (2007): DEB‑consistent formulation

Below I **extract and formalize the larval diets used in Kaun et al. (2007)** and translate them into **DEB‑consistent substrate descriptions**, ending with a **single derived quantity** — the **energy density of food** \(\varepsilon_X\) in **J·cm⁻³** — which can be used consistently to parameterize functional response and assimilation in DEB models.

Throughout, we explicitly separate:
- **DEB food density** \(X\) (substrate density, e.g. C‑mol·cm⁻³),
- **chemical potential** \(\mu_X\) (J·C‑mol⁻¹), and
- the **derived environmental energy density**
\[
\boxed{\varepsilon_X \equiv \mu_X\,X \qquad [\varepsilon_X]=\mathrm{J\,cm^{-3}}}
\]
This quantity is *not* a new DEB state variable; it is a **defined product** that is useful when food recipes are given by mass or molarity.

---

## 1. Diets detected in Kaun et al. (2007)

Kaun et al. use **three classes of larval food substrates**, depending on the experiment:

1. **Standard rearing medium** (yeast–sucrose–agar), sometimes diluted (100%, 75%, 50%, 25%, 15%)
2. **Yeast paste** (used in feeding and absorption assays)
3. **Defined sugar–agarose substrates** (used as test foods)
   - glucose–agarose
   - fructose–agarose

Only (1) and (2) are nutritionally complete. The sugar–agarose substrates are **single‑compound carbon sources**, used to probe feeding behavior rather than growth.

---

## 2. Notational conventions used here (important)

To avoid confusion, we enforce the following throughout:

- \(X\) : DEB food density (substrate), unit chosen consistently with \(K\)
- \(\mu_X\) : chemical potential of food (J·C‑mol⁻¹)
- \(\varepsilon_X = \mu_X X\) : **energy per volume of substrate** (J·cm⁻³)

When the paper specifies **recipes in g·L⁻¹ or mol·L⁻¹**, we first compute \(\varepsilon_X\) via **mass concentrations**, using:
\[
\varepsilon_X = \sum_i \rho_i\, e_i
\]
where:
- \(\rho_i\) = mass concentration of ingredient \(i\) (g·cm⁻³)
- \(e_i\) = gross energy content of ingredient \(i\) (J·g⁻¹)

Conversion to \(X\) (e.g. C‑mol·cm⁻³) can be done later if needed.

---

## 3. Diet 1 — Standard rearing medium

### 3.1 Composition (per liter of water)

| Component | Amount (g·L⁻¹) | Role |
|---|---:|---|
| Baker’s yeast | 50 | protein, lipid, carbohydrate |
| Sucrose | 100 | carbohydrate |
| Agar | 16 | gelling agent (non‑assimilable) |
| KPO₄ | 0.1 | mineral |
| NaK‑tartrate | 8 | mineral |
| NaCl | 0.5 | mineral |
| MgCl₂ | 0.5 | mineral |
| Fe₂(SO₄)₃ | 0.5 | mineral |
| Water | balance | solvent |

Only **yeast and sucrose** contribute significantly to assimilable energy.

Food quality manipulations (25%, 15%, etc.) scale **yeast + sucrose together**.

---

### 3.2 Energy density of the standard medium

Assume:
- aqueous gel, bulk density \(\rho_{\text{medium}} \approx 1\,\mathrm{g\,cm^{-3}}\)
- agar contributes negligible assimilable energy

Energy per mass (typical values):
- yeast: \(e_Y \approx 21\times10^3\,\mathrm{J\,g^{-1}}\)
- sucrose: \(e_S \approx 16.5\times10^3\,\mathrm{J\,g^{-1}}\)

Energy per liter:
\[
E_{\text{yeast}} = 50\times21 = 1050\;\mathrm{kJ}
\]
\[
E_{\text{sucrose}} = 100\times16.5 = 1650\;\mathrm{kJ}
\]
\[
E_{\text{total}} = 2700\;\mathrm{kJ\,L^{-1}}
\]

Thus the **energy density of the standard medium** is:
\[
\boxed{
\varepsilon_X^{\text{standard}}
= \frac{2.7\times10^6}{1000}
\approx 2.7\times10^3\;\mathrm{J\,cm^{-3}}
}
\]

For diluted food (quality factor \(q\)):
\[
\varepsilon_X(q) = q\,\varepsilon_X^{\text{standard}}
\]

---

## 4. Diet 2 — Yeast paste

### 4.1 Composition

The yeast paste is prepared as **2:1 water:yeast (w/w)**.

Mass fraction of yeast:
\[
w_Y = \frac{1}{3}
\]

Assuming slurry density \(\approx 1\,\mathrm{g\,cm^{-3}}\):
\[
\rho_Y = w_Y\,\rho_{\text{paste}} = 0.333\;\mathrm{g\,cm^{-3}}
\]

---

### 4.2 Energy density

With yeast energy per mass \(e_Y = 21\times10^3\,\mathrm{J\,g^{-1}}\):
\[
\boxed{
\varepsilon_{X,\text{yeast paste}}
= \rho_Y\, e_Y
= 0.333\times21\times10^3
\approx 7.0\times10^3\;\mathrm{J\,cm^{-3}}
}
\]

Unit check:
\(\mathrm{g\,cm^{-3}}\times\mathrm{J\,g^{-1}} = \mathrm{J\,cm^{-3}}\).

---

## 5. Diet 3 — Sugar–agarose substrates

These substrates are **not nutritionally complete** and should be treated as **single‑compound DEB foods**.

### 5.1 Glucose–agarose

Recipe: **10% glucose (w/v)**, 2.3% agarose.

Mass concentration:
\[
\rho_G = 0.10\;\mathrm{g\,cm^{-3}}
\]

With glucose energy per mass \(e_G = 15.6\times10^3\,\mathrm{J\,g^{-1}}\):
\[
\boxed{
\varepsilon_{X,\text{glucose}}
= \rho_G\, e_G
= 0.10\times15.6\times10^3
= 1.56\times10^3\;\mathrm{J\,cm^{-3}}
}
\]

---

### 5.2 Fructose–agarose

Recipe: **2 mol·L⁻¹ fructose**, 1% agarose.

Molar mass:
\[
M_F = 180\;\mathrm{g\,mol^{-1}}
\]

Mass concentration:
\[
\rho_F = \frac{2\times180}{1000} = 0.36\;\mathrm{g\,cm^{-3}}
\]

With carbohydrate energy per mass \(e_F \approx 15.6\times10^3\,\mathrm{J\,g^{-1}}\):
\[
\boxed{
\varepsilon_{X,\text{fructose}}
= 0.36\times15.6\times10^3
\approx 5.6\times10^3\;\mathrm{J\,cm^{-3}}
}
\]

---

## 6. DEB assimilation equations (isomorph with rod shape correction)

### 6.1 Morphological assumption

Drosophila larvae are treated as **isomorphs with a rod‑like shape correction**:

- structural volume: \(V = L^3\)
- physical length: \(L_{\text{phys}} = \delta_M L\)
- assimilation surface \(\propto \delta_M^2 L^2\)

The shape coefficient \(\delta_M\) is constant and absorbed into assimilation parameters.

---

### 6.2 Assimilation

Standard DEB assimilation for an isomorph:
\[
\dot p_A = \{\dot p_{Am}\}\, f\, L^2
\]

with functional response:
\[
f = \frac{X}{K+X} = \frac{\varepsilon_X}{\varepsilon_K+\varepsilon_X},
\qquad \varepsilon_K \equiv \mu_X K
\]

Including rod shape correction:
\[
\boxed{
\dot p_A
= \{\dot p_{Am}\}^{\text{rod}}\, f\, L^2,
\qquad
\{\dot p_{Am}\}^{\text{rod}} = \delta_M^2\,\{\dot p_{Am}\}
}
\]

This formulation is **DEB‑consistent**, diet‑specific via \(\varepsilon_X\), and directly applicable to larval growth on any of the diets above.

---

## 7. Summary: single food energy densities

| Diet | \(\varepsilon_X\) (J·cm⁻³) | Notes |
|---|---:|---|
| Standard medium (100%) | \(2.7\times10^3\) | complete diet |
| Standard medium (q) | \(q\times2.7\times10^3\) | dilution series |
| Yeast paste | \(7.0\times10^3\) | high‑quality reference |
| Glucose–agarose | \(1.56\times10^3\) | carbon‑only test |
| Fructose–agarose | \(5.6\times10^3\) | carbon‑only test |

---

**End of file — Diets_Kaun2007.md**

