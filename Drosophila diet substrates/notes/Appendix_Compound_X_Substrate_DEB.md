# Appendix. 

# DEB Formulation for a single compound X in a substrate

In DEB theory, compounds are quantified on a carbon-molar basis to ensure consistency between chemical composition, thermodynamic potential, and energetic bookkeeping. For a compound X with empirical formula \( \mathrm{C}_{n_C}\mathrm{H}_{n_H}\mathrm{O}_{n_O}\mathrm{N}_{n_N} \), the carbon content defines the fundamental counting unit: one C-mol (carbon mole) is the amount of compound that contains one mole of carbon atoms. Thus, 1 mol of compound contains \( n_C \) C-moles. All concentrations refer to the substrate in which compound X is present.

Following DEB convention, the carbon-molar concentration is denoted by \( X \), while the corresponding mass concentration of compound X in the substrate is denoted by \( c_X \) (g cm⁻³). The relations between chemical composition, concentration, chemical potential, and resulting energy density due exclusively to compound X are summarized in Table A1.

---

| Symbol | Description | Unit | Defining equation |
|--------|-------------|------|-------------------|
| \( w \) | Molar mass of compound X | g mol⁻¹ | \( w = 12 n_C + 1 n_H + 16 n_O + 14 n_N \) |
| \( w_C \) | Molar mass per C-mol of compound X | g C-mol⁻¹ | \( w_C = \dfrac{w}{n_C} \) |
| \( c_X \) | Mass concentration of compound X in the substrate | g cm⁻³ | — |
| \( X \) | Carbon-molar concentration of compound X in the substrate | C-mol cm⁻³ | \( X = \dfrac{c_X}{w_C} \) |
| \( \mu_X \) | Chemical potential of compound X (per C-mol) | J C-mol⁻¹ | — |
| \( e_X \) | Energy per gram of compound X | J g⁻¹ | \( e_X = \dfrac{\mu_X}{w_C} \) |
| \( \varepsilon_X \) | Energy density due to compound X in the substrate | J cm⁻³ | \( \varepsilon_X = \mu_X X = e_X c_X \) |

**Table A1.** Definitions and relations for compound X in a substrate under the carbon-molar formulation of DEB theory. Energy densities refer exclusively to the energetic contribution of compound X.

---

# Frequently used dietary compounds in *Drosophila* media

Edible components of *Drosophila* diet media are characterized by their empirical formula and their chemical potential \( \mu_X \), from which their molar mass \( w \) and energetic variables \( e_X, \varepsilon_X \) can be derived (see Table A1). Non-edible structural components of the substrate (e.g. agar) are excluded since they do not contribute metabolizable energy. The most commonly used energetically meaningful compounds are shown in Table A2.

---

| Compound | Empirical formula \( \mathrm{C}_{n_C}\mathrm{H}_{n_H}\mathrm{O}_{n_O}\mathrm{N}_{n_N} \) | Molar mass \( w \) (g mol⁻¹) | Chemical potential \( \mu_X \) (kJ C-mol⁻¹) | Energy per gram \( e_X \) (kJ g⁻¹) |
|-----------|--------------------------------------------------|----------------------|----------------------------------|-----------------------------|
| **Glucose / Fructose / Dextrose** | C\(_6\)H\(_{12}\)O\(_6\) | 180.16 | 468 | 15.6 |
| **Sucrose** | C\(_{12}\)H\(_{22}\)O\(_{11}\) | 342.30 | 471 | 16.5 |
| **Starch** (repeat unit) | (C\(_6\)H\(_{10}\)O\(_5\))\(_n\) | 162.14 (monomer) | 459 | 17.0 |
| **Brewer’s yeast (dry)** | ≈ C\(_{4.5}\)H\(_{7.3}\)O\(_{2.2}\)N\(_{0.8}\) | ≈113 (empirical mol) | 478 | 19.0 |
| **Propionic acid** | C\(_3\)H\(_6\)O\(_2\) | 74.08 | 513 | 20.8 |

**Table A2.** Chemical composition and energetic properties of edible compounds used in *Drosophila* diet media.