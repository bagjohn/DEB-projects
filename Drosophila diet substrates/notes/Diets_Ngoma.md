# Ngoma_diets

Diet extraction and DEB-style conversion for  
**Ng’oma et al. (2019)** – *The evolutionary potential of diet-dependent effects on lifespan and fecundity in a multi-parental population of Drosophila melanogaster*

---

## 1. Source and scope

This file extracts the **adult diets** used in Ng’oma et al. (2019) and converts them into **Dynamic Energy Budget (DEB)** food descriptors following the standard pipeline:

\[
\text{recipe} \;\rightarrow\; \rho_i \;\rightarrow\; \varepsilon_X,\; X,\; \mu_X
\]

Diets included:
- **DR** – Dietary restriction  
- **C** – Control  
- **HS** – High sugar  

The **maintenance diet** is listed in Table S1 of the paper but is **not used** in the lifespan/fecundity experiment and is therefore excluded from DEB calculations here.

---

## 2. Table S1 – Diet recipes (as reported)

### Table S1. The four diets used in the experiment

| Ingredient | Maintenance | DR | C | HS |
|---|---:|---:|---:|---:|
| Water (ml) | 1066 | 1000 | 1000 | 1000 |
| Agar (g) | 6.25 | 10 | 10 | 10 |
| Dextrose (g) | 86.26 | - | - | - |
| Sucrose (g) | - | 50 | 50 | 342 |
| Molarity | - | 0.15 | 0.15 | 1 |
| Yeast (g) | 21.6 | 100 | 200 | 200 |
| Cornmeal (g) | 40.8 | – | – | – |
| Tegosept (g) | 1.8 | 2.7 | 2.7 | 2.7 |
| Ethanol (ml) | 7.3 | 11 | 11 | 11 |
| % Protein | 10-13 | 36-41 | 45-53 | 17-19 |
| % Carbohydrate | 93-95 | 59-64 | 47-52 | 81-83 |

---

## 3. DEB conversion assumptions

Following the standard DEB diet-extraction tutorial:

### Edible vs inert components
- **Edible (counted):**
  - Yeast
  - Sucrose
- **Inert (ignored energetically):**
  - Agar, cornmeal, Tegosept, ethanol, water

### Constants
- Energy density of yeast:  
  \[
  e_Y = 21{,}000\ \mathrm{J\ g^{-1}}
  \]
- Energy density of sugar (sucrose):  
  \[
  e_S = 15{,}600\ \mathrm{J\ g^{-1}}
  \]
- Carbon mass per C-mol:
  \[
  w_{C,Y} = 24.63\ \mathrm{g\ C\text{-}mol^{-1}},\quad
  w_{C,S} = 28.52\ \mathrm{g\ C\text{-}mol^{-1}}
  \]
- Total diet volume:  
  \[
  V \approx 1\ \mathrm{L} = 1000\ \mathrm{cm^3}
  \]

---

## 4. Recipe → mass concentrations

Mass concentrations \(\rho_i = m_i / V\)

### Dietary Restriction (DR)
- Yeast: 100 g → \(\rho_Y = 0.100\ \mathrm{g\ cm^{-3}}\)
- Sucrose: 50 g → \(\rho_S = 0.050\ \mathrm{g\ cm^{-3}}\)

### Control (C)
- Yeast: 200 g → \(\rho_Y = 0.200\ \mathrm{g\ cm^{-3}}\)
- Sucrose: 50 g → \(\rho_S = 0.050\ \mathrm{g\ cm^{-3}}\)

### High Sugar (HS)
- Yeast: 200 g → \(\rho_Y = 0.200\ \mathrm{g\ cm^{-3}}\)
- Sucrose: 342 g → \(\rho_S = 0.342\ \mathrm{g\ cm^{-3}}\)

---

## 5. Environmental energy density εX

\[
\varepsilon_X = \sum_i \rho_i e_i
\]

| Diet | Yeast (J cm⁻³) | Sugar (J cm⁻³) | **εX total (J cm⁻³)** |
|---|---:|---:|---:|
| DR | 2100 | 780 | **2.88 × 10³** |
| C  | 4200 | 780 | **4.98 × 10³** |
| HS | 4200 | 5335 | **9.54 × 10³** |

---

## 6. DEB food density X (C-mol cm⁻³)

\[
X = \sum_i \frac{\rho_i}{w_{C,i}}
\]

| Diet | Yeast | Sugar | **X total (C-mol cm⁻³)** |
|---|---:|---:|---:|
| DR | 4.06 × 10⁻³ | 1.75 × 10⁻³ | **5.82 × 10⁻³** |
| C  | 8.12 × 10⁻³ | 1.75 × 10⁻³ | **9.87 × 10⁻³** |
| HS | 8.12 × 10⁻³ | 1.20 × 10⁻² | **2.01 × 10⁻²** |

---

## 7. Chemical potential of food µX

\[
\mu_X = \frac{\varepsilon_X}{X}
\]

| Diet | **µX (J C-mol⁻¹)** |
|---|---:|
| DR | **4.95 × 10⁵** |
| C  | **5.05 × 10⁵** |
| HS | **4.75 × 10⁵** |

---

## 8. Final DEB-ready summary

| Diet | εX (J cm⁻³) | X (C-mol cm⁻³) | µX (J C-mol⁻¹) | Interpretation |
|---|---:|---:|---:|---|
| DR | 2.88e3 | 5.82e-3 | 4.95e5 | Yeast restriction, pure dilution |
| C  | 4.98e3 | 9.87e-3 | 5.05e5 | Reference control diet |
| HS | 9.54e3 | 2.01e-2 | 4.75e5 | High sugar, lower effective quality |

---

## 9. DEB interpretation notes

- **DR vs C**  
  \[
  X_{DR} \approx 0.59\,X_C,\qquad \mu_X \approx \text{constant}
  \]  
  → classic **dietary restriction as food dilution**

- **HS vs C**  
  \[
  X_{HS} \approx 2.0\,X_C,\qquad \mu_X \downarrow
  \]  
  → carbohydrate-heavy diet, explaining reduced lifespan and fecundity despite high energy availability

These descriptors can be used directly in functional-response formulations:
\[
f = \frac{X}{K + X} = \frac{\varepsilon_X}{\varepsilon_K + \varepsilon_X}
\]

---

**End of file: `Ngoma_diets.md`**
