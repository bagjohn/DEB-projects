# Appendix: Chemical Potential and Glucose Absorption in *Kaun et al.* (2007)

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

This appendix merges and harmonizes material on chemical potential and tracer-based glucose absorption into a single DEB-consistent reference document. It is intended as a methods/appendix section for manuscripts, theses, or model documentation.

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

Thus the diet is mixed and nutritionally complete, glucose is not the sole nutrient, and the tracer probes carbohydrate-specific ingestion and retention rather than total feeding or total assimilation.

For DEB energetics in this appendix, we therefore treat yeast paste as the energetically dominant substrate and the ¹⁴C-glucose signal as a marker variable. Since *Kaun et al.* (2007) do not report a tracer mass/volume density for conversion to an absolute dietary energy contribution, the tracer itself is not used as a separate energetic input in the DEB budget here.

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

## A5. Absorption efficiency proxy

A robust, dimensionless quantity summarising the tracer assay is the absorption (retention) fraction:

$$
\eta_{\mathrm{abs}} = \frac{\text{Absorption}}{\text{Intake}}
$$

Using the digitized values gives:

| Genotype | $\eta_{\mathrm{abs}}$ |
|---|---:|
| forᴿ | 0.516 |
| forˢ | 0.161 |
| forˢ² | 0.174 |

Interpretation used in this appendix (explicit assumptions):

1. Retention is treated as a proxy for effective assimilation in the measured pathway (retained tracer is assumed to have entered assimilated metabolic processing).
2. Genotype ranking from carbohydrate retention is transferred to a unified effective assimilation efficiency used for the yeast-paste diet in DEB simulations.
3. Tracer-based intake/retention is mapped to yeast-paste intake/retention through a genotype-invariant proportionality factor, because direct yeast-labelled measurements are unavailable.

---

## A6. Conversion to C-moles and energy (tracer and yeast-proxy)

We use:
- glucose: $n_C = 6$
- $1\,\mathrm{fmol} = 10^{-15}\,\mathrm{mol}$

For a value $B$ (fmol glucose per larva), the tracer-carbon amount and tracer-linked energy are:

$$
 n_{C,\mathrm{tr}} = 6\,B\times10^{-15}\quad [\mathrm{C\!\!\text{-}mol}]
$$

$$
 E_{\mathrm{tr}} = \mu_{\mathrm{carb}}\, n_{C,\mathrm{tr}} \quad [\mathrm{J}]
$$

Using the digitized absorption values, we obtain:

| Genotype | Absorption (fmol) | $n_{C,\mathrm{tr}}$ (C-mol·larva⁻¹) | $E_{\mathrm{tr}}$ (J·larva⁻¹) |
|---|---:|---:|---:|
| forᴿ | 309.68 | $1.86\times10^{-12}$ | $8.70\times10^{-7}$ |
| forˢ | 193.55 | $1.16\times10^{-12}$ | $5.43\times10^{-7}$ |
| forˢ² | 182.49 | $1.09\times10^{-12}$ | $5.12\times10^{-7}$ |

These energies are tracer-linked and not the dominant dietary energy term of yeast paste.

To connect tracer measurements to DEB energetics of yeast paste, define:

$$
\phi_Y \equiv \frac{n_{C,\mathrm{yeast\text{-}eq}}}{n_{C,\mathrm{tr}}}
$$

and yeast-equivalent retained energy:

$$
E_{Y,\mathrm{eq}} = \mu_Y\,\phi_Y\,n_{C,\mathrm{tr}}
$$

With baseline proxy $\phi_Y=1$ and $\mu_Y\approx\mu_{\mathrm{carb}}$, the yeast-equivalent retained-energy table equals the tracer table above; for calibrated $\phi_Y$, all entries scale linearly by $\phi_Y$.

---

## A7. Average fluxes (DEB-style interpretation)

Taking the 15 min feeding window as:

$$
\Delta t_{\mathrm{feed}} = 15\,\mathrm{min} = 0.0104167\,\mathrm{d}
$$

we define the average ingestion flux of glucose-derived carbon as:

$$
\dot J_X^{(15)} = \frac{n_{C,\mathrm{intake}}}{\Delta t_{\mathrm{feed}}}
$$

while the average net absorbed flux is:

$$
\dot J_{\mathrm{abs}}^{(15)} = \frac{n_{C,\mathrm{abs}}}{\Delta t_{\mathrm{feed}}}
$$

The corresponding energy flux is:

$$
\dot p = \mu_{\mathrm{carb}}\,\dot J
$$

---

## A8. DEB-consistent placement

In DEB terms, the main points are:

- Functional response must be computed explicitly:

$$
f = \frac{X}{X+K}
$$

so $f$ is not set a priori from qualitative high-food arguments.

- The half-saturation coefficient is:

$$
K = \frac{\{\dot J_{Xm}\}}{\{\dot F_m\}} = \frac{\{\dot p_{Am}\}}{\kappa_X\,\mu_X\,\{\dot F_m\}}
$$

with $\{\dot p_{Am}\}=\kappa_X\mu_X\{\dot J_{Xm}\}$.

- If maximum ingestion is shared across genotypes, genotype differences in effective assimilation efficiency $\kappa_X$ imply genotype differences in $K$:

$$
K_i = \frac{\{\dot p_{Am}\}_i}{\kappa_{X,i}\,\mu_X\,\{\dot F_m\}_i}
$$

and under common $\{\dot p_{Am}\}$ and $\{\dot F_m\}$ assumptions:

$$
\frac{K_i}{K_j} = \frac{\kappa_{X,j}}{\kappa_{X,i}}
$$

- Therefore tracer data constrain relative genotype differences in effective assimilation (through $\eta_{\mathrm{abs}}$ and mapping assumptions), while absolute energetic scaling is anchored by yeast-paste energy density.

A DEB-consistent workflow is: use yeast paste as energetic substrate, estimate genotype-specific $\kappa_X$ modifiers from tracer retention ratios under explicit assumptions, and compute $f$ dynamically from $X$ and genotype-specific $K$.

---

**End of appendix**

