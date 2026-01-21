# F424 and JAZZ Diets — DEB-Compatible Extraction and Comparison

This document consolidates the full pipeline discussed in this thread into a **single, non-redundant, DEB-ready summary**.  
It extracts the two experimental diets (**F424** and **JAZZ**) from *Ormerod et al. (2017)*, converts them into **absolute DEB food descriptors**, and summarizes their **mechanistic differences** in Dynamic Energy Budget (DEB) terms.

---

## 1. Experimental source and context

- Study: *Drosophila development, physiology, behavior, and lifespan are influenced by altered dietary composition*  
  (Ormerod et al., 2017)
- Organism: *Drosophila melanogaster* (Canton-S)
- Diets compared:
  - **Formula 4-24® (F424)** — Carolina Biological
  - **Jazz-mix® (JAZZ)** — Fisher Scientific
- Diets used across all life stages, with ≥4 generations of acclimation.

---

## 2. Diet composition and DEB abstraction

### 2.1 Ingredient-level interpretation

**Edible (count toward DEB food X):**
- Yeast
- Sugars (sucrose / “sugar”)
- Starches, maize meal, flours  
→ pooled into a **single effective substrate X**

**Inert (excluded from X):**
- Water, agar
- Minerals, ash
- Vitamins, preservatives, acids, colorants

This follows standard DEB practice: only energy-bearing organic matter contributes to food density and energy density.

---

## 3. Quantitative proximate composition (wet mass basis)

From Table 2 of Ormerod et al. (2017), wet percentages are treated as g cm⁻³ assuming bulk density ≈ 1 g cm⁻³.

| Diet | Protein | Fat | Carbohydrate |
|-----|---------|-----|--------------|
| **F424** | 0.0191 | 0.0012 | 0.2119 |
| **JAZZ** | 0.0080 | 0.0001 | 0.1701 |

Moisture and ash are excluded from DEB food calculations.

---

## 4. Assumptions for DEB conversion

Macronutrient proxies (DEB textbook conventions):

- **Carbohydrates** (CH₂O):  
  \( e = 17.2 \ \text{kJ g}^{-1} \), \( w_C = 30.0 \ \text{g C-mol}^{-1} \)

- **Proteins** (CH₁.₆₁O₀.₃₃N₀.₂₈):  
  \( e = 17.6 \ \text{kJ g}^{-1} \), \( w_C = 22.81 \ \text{g C-mol}^{-1} \)

- **Lipids** (CH₁.₉₂O₀.₁₂):  
  \( e = 38.9 \ \text{kJ g}^{-1} \), \( w_C = 15.84 \ \text{g C-mol}^{-1} \)

Mixture formulas:

\[
\varepsilon_X = \sum_i \rho_i e_i
\]
\[
X = \sum_i \frac{\rho_i}{w_{C,i}}
\]
\[
\mu_X = \frac{\varepsilon_X}{X}
\]

---

## 5. Absolute DEB food descriptors

### 5.1 Results

| Diet | εX (J cm⁻³) | X (C-mol cm⁻³) | μX (J C-mol⁻¹) |
|-----|-------------:|---------------:|---------------:|
| **F424** | 4.03 × 10³ | 7.98 × 10⁻³ | 5.05 × 10⁵ |
| **JAZZ** | 3.07 × 10³ | 6.03 × 10⁻³ | 5.09 × 10⁵ |

### 5.2 Interpretation

- **μX is effectively identical** between diets  
  (\(\mu_X \approx 5 × 10^5 \ \text{J C-mol}^{-1}\))  
  → no meaningful difference in intrinsic food quality.
- Differences arise primarily through **X** and **εX**:
  - F424 is ~30% more energy-dense per unit volume than JAZZ.

---

## 6. Biological outcome and DEB interpretation

Empirical results from the paper:
- Higher ingestion rates on **JAZZ**
- Faster development, larger size, longer lifespan on **JAZZ**
- Reduced performance on **F424**

DEB-level interpretation:
- **F424**: higher nominal εX, but lower realized intake → functionally limiting food.
- **JAZZ**: lower εX, but higher feeding rates → higher realized assimilation flux \( \dot p_A \).

Thus, the diets differ **not in food quality (μX)**, but in **effective accessibility and functional response (f)**.

---

## 7. DEB-level conclusion

> **F424 and JAZZ differ primarily in food density and accessibility, not in food quality.  
> F424 is energetically richer per volume, but JAZZ supports a higher functional response and thus a higher realized assimilation flux.**

This makes the F424–JAZZ comparison a clean experimental case for separating:
- food quality (μX),
- food density (X, εX),
- and feeding regulation (behavioral/physiological control of f).

---

## 8. Ready-to-use DEB encoding (example)

```matlab
% Absolute DEB food descriptors
food.F424.epsX = 4.03e3;   % J/cm^3
food.F424.X    = 7.98e-3;  % C-mol/cm^3
food.F424.muX  = 5.05e5;   % J/C-mol

food.JAZZ.epsX = 3.07e3;
food.JAZZ.X    = 6.03e-3;
food.JAZZ.muX  = 5.09e5;
