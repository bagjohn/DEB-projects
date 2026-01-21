# Larvaworld nutrition: compounds, substrates, quality, and nutrient concentration X

This note derives the equations implemented in `larvaworld/lib/param/composition.py` for **Compound** and **Substrate**, and computes the substrate nutrient concentration **X** at **q = 1** for each built-in substrate type.


## 0. Compounds

<table style="border-collapse: collapse;">
	<tr>
		<th style="border: 1px solid #666; padding: 4px;">compound</th>
		<th style="border: 1px solid #666; padding: 4px;">n<sub>C</sub></th>
		<th style="border: 1px solid #666; padding: 4px;">n<sub>H</sub></th>
		<th style="border: 1px solid #666; padding: 4px;">n<sub>O</sub></th>
		<th style="border: 1px solid #666; padding: 4px;">n<sub>N</sub></th>
		<th style="border: 1px solid #666; padding: 4px;">w<sub>computed</sub> (g·mol<sup>-1</sup>)</th>
		<th style="border: 1px solid #666; padding: 4px;">w (g·mol<sup>-1</sup>)</th>
	</tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">glucose</td><td style="border: 1px solid #666; padding: 4px;">6</td><td style="border: 1px solid #666; padding: 4px;">12</td><td style="border: 1px solid #666; padding: 4px;">6</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">180</td><td style="border: 1px solid #666; padding: 4px;">180.18</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">dextrose</td><td style="border: 1px solid #666; padding: 4px;">6</td><td style="border: 1px solid #666; padding: 4px;">12</td><td style="border: 1px solid #666; padding: 4px;">7</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">197</td><td style="border: 1px solid #666; padding: 4px;">198.17</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">saccharose</td><td style="border: 1px solid #666; padding: 4px;">12</td><td style="border: 1px solid #666; padding: 4px;">22</td><td style="border: 1px solid #666; padding: 4px;">11</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">343</td><td style="border: 1px solid #666; padding: 4px;">342.30</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">yeast</td><td style="border: 1px solid #666; padding: 4px;">19</td><td style="border: 1px solid #666; padding: 4px;">14</td><td style="border: 1px solid #666; padding: 4px;">2</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">268</td><td style="border: 1px solid #666; padding: 4px;">274.3</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">agar</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">38</td><td style="border: 1px solid #666; padding: 4px;">19</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">613</td><td style="border: 1px solid #666; padding: 4px;">336.33</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">cornmeal</td><td style="border: 1px solid #666; padding: 4px;">27</td><td style="border: 1px solid #666; padding: 4px;">48</td><td style="border: 1px solid #666; padding: 4px;">20</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">628</td><td style="border: 1px solid #666; padding: 4px;">359.33</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">water</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">2</td><td style="border: 1px solid #666; padding: 4px;">1</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">18</td><td style="border: 1px solid #666; padding: 4px;">18.01528</td></tr>
	<caption style="caption-side: bottom;">Table 1. Compound properties: molecular weight, stoichiometry, ww proxy</caption>
</table>


For each compound \(c\), the class defines:
- Density: \(d_c\) in g·cm\(^{-3}\) (used in substrate compositions).
- Atom counts: \(n_{C,c}, n_{H,c}, n_{O,c}, n_{N,c}\).
- Carbon-equivalent proxy:
$$
ww_c = n_{C,c} + \frac{n_{H,c}}{12} + \frac{16\,n_{O,c}}{12} + \frac{14\,n_{N,c}}{12}.
$$
Here \(ww_c\) is removed from the table (not used further). Molecular weight \(w_c\) (g·mol\(^{-1}\)) is provided per compound; a computed estimate from atom counts is
$$
w_{c,\text{computed}} = 12\,n_{C,c} + 1\,n_{H,c} + 16\,n_{O,c} + 14\,n_{N,c},
$$
using standard atomic masses (g·mol\(^{-1}\)).

## 1. Substrate presets: composition table (g·cm⁻³)

<table style="border-collapse: collapse;">
	<tr>
		<th style="border: 1px solid #666; padding: 4px;">substrate</th>
		<th style="border: 1px solid #666; padding: 4px;">glucose</th>
		<th style="border: 1px solid #666; padding: 4px;">dextrose</th>
		<th style="border: 1px solid #666; padding: 4px;">saccharose</th>
		<th style="border: 1px solid #666; padding: 4px;">yeast</th>
		<th style="border: 1px solid #666; padding: 4px;">cornmeal</th>
		<th style="border: 1px solid #666; padding: 4px;">agar</th>
		<th style="border: 1px solid #666; padding: 4px;">source</th>
	</tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">agar</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.016</td><td style="border: 1px solid #666; padding: 4px;">-</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">standard</td><td style="border: 1px solid #666; padding: 4px;">0.1</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.05</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.016</td><td style="border: 1px solid #666; padding: 4px;">Kaun et al., 2008</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">sucrose</td><td style="border: 1px solid #666; padding: 4px;">0.0171</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.004</td><td style="border: 1px solid #666; padding: 4px;">-</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">cornmeal</td><td style="border: 1px solid #666; padding: 4px;">0.03041</td><td style="border: 1px solid #666; padding: 4px;">0.06076</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.10094</td><td style="border: 1px solid #666; padding: 4px;">0.00547</td><td style="border: 1px solid #666; padding: 4px;">-</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">cornmeal2</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.07031</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.01406</td><td style="border: 1px solid #666; padding: 4px;">0.06563</td><td style="border: 1px solid #666; padding: 4px;">0.00656</td><td style="border: 1px solid #666; padding: 4px;">-</td></tr>
	<tr><td style="border: 1px solid #666; padding: 4px;">PED_tracker</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">0.01</td><td style="border: 1px solid #666; padding: 4px;">0.1875</td><td style="border: 1px solid #666; padding: 4px;">-</td><td style="border: 1px solid #666; padding: 4px;">5</td><td style="border: 1px solid #666; padding: 4px;">Wosniack et al., 2021</td></tr>
	<caption style="caption-side: bottom;">Table 2. Substrate composition : compound densities in g·cm⁻³</caption>
</table>

Dashes indicate absent compounds in that preset; all numbers are densities in g·cm⁻³.


## 2. Substrate model

A substrate is defined by:

- a composition dictionary \(\{d_c\}\) with entries in **g·cm⁻³**

- a quality factor \(q\in[0,1]\) that reduces nutrient availability

- a fixed water density used internally: \(d_{\mathrm{water}}=1\,\mathrm{g\,cm^{-3}}\)


### 2.1 Sets of compounds

From the file:

- **all compounds**: all listed compounds except water

- **nutritious compounds** \(\mathcal N\): all compounds except **water** and **agar**


### 2.2 Nutrient mass density \(d_X\)

By default, nutrients are the sum over nutritious compounds, multiplied by quality:

$$
 d_X(q) = q\,\sum_{c\in\mathcal N} d_c
$$

Units: \([d_X]=\mathrm{g\,cm^{-3}}\).

### 2.3 Density-weighted nutrient proxy \(w_X\)

The code computes a density-weighted mean of `ww` using **quality = 1** (important):

$$
 w_X = \frac{\sum_{c\in\mathcal N} d_c\,ww_c}{\sum_{c\in\mathcal N} d_c}
$$

Units: dimensionless (it is an average of dimensionless \(ww_c\)).

### 2.4 Nutrient concentration \(X\)

The substrate nutrient concentration returned by `Substrate.get_X()` is:

$$
 X(q) = \frac{d_X(q)}{w_X}
$$

Units (as used by the model): **mol·cm⁻³** in the code’s “molar-equivalent” convention.
This is the quantity later used in the DEB-like functional response:

$$
 f = \frac{X}{K+X}
$$


### 2.5 Total molar concentration \(C\) and nutrient ratio

The code also defines:

$$
 C(q) = \frac{d_{\mathrm{water}}}{w_{\mathrm{water}}} + X_{\mathrm{all}}(q)
$$

where \(X_{\mathrm{all}}\) is computed like \(X\) but summing over **all compounds** (including agar, excluding water).
Then:

$$
 X_{\mathrm{ratio}}(q) = \frac{X(q)}{C(q)}
$$


## 3. Built-in substrate types and compositions

The file defines the following substrate presets (densities in g·cm⁻³):

- **agar**: agar=0.016
- **standard**: glucose=0.1, yeast=0.05, agar=0.016
- **sucrose**: glucose=0.0171, agar=0.004
- **cornmeal**: glucose=0.0304118, dextrose=0.0607647, cornmeal=0.100941, agar=0.00547059
- **cornmeal2**: dextrose=0.0703125, yeast=0.0140625, cornmeal=0.065625, agar=0.0065625
- **PED_tracker**: saccharose=0.01, yeast=0.1875, agar=5

## 4. Computed X for each substrate at q = 1

Using the exact equations above, with \(q=1\) and \(\mathcal N =\) all compounds except water and agar, the computed values are:

| substrate | d_X(q=1) (g·cm⁻³) | w_X (dimensionless) | X(q=1) (mol·cm⁻³, model units) |
|---|---:|---:|---:|
| PED_tracker | 0.1975 | 23.1203 | 0.00854229 |
| agar | 0 | 0 | 0 |
| cornmeal | 0.192118 | 37.8394 | 0.00507719 |
| cornmeal2 | 0.15 | 35.026 | 0.00428253 |
| standard | 0.15 | 17.6111 | 0.00851735 |

For the DEB feeding-rate expressions, the relevant food energy-per-volume term is
$$
\Phi_X = \mu_X\,X,
$$
so for the numeric values above (in model units) the corresponding $\Phi_X$ values are simply $\mu_X$ times the tabulated $X(q=1)$; set $\mu_X$ according to your food energy density.

## Diets retrieved from web

| Compound (as used in diet recipes)    | Edible by larvae? | Chemical formula (or DEB proxy)                         | Molar mass (g/mol) | CHON per C-mol | w<sub>C</sub> (g per C-mol) | Source                                                                    |
| ------------------------------------- | ----------------: | ------------------------------------------------------- | -----------------: | -------------- | ------------------: | ------------------------------------------------------------------------- |
| Sucrose (“Sugar”)                     |               Yes | C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>              |             342.30 | C<sub>1</sub>H<sub>1.833</sub>O<sub>0.917</sub>N<sub>0</sub> |               28.52 | Skorupa diet recipes use “Sugar (g·dl<sup>-1</sup>)”.                     |
| Dextrose (glucose)                    |               Yes | C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>                |             180.16 | C<sub>1</sub>H<sub>2</sub>O<sub>1</sub>N<sub>0</sub>         |               30.03 | Skorupa larval media lists “Dextrose 55 g”.                               |
| Brewer’s yeast (food biomass proxy)   |               Yes | **DEB biomass proxy**: C<sub>1</sub>H<sub>1.8</sub>O<sub>0.5</sub>N<sub>0.2</sub> |                  — | C<sub>1</sub>H<sub>1.8</sub>O<sub>0.5</sub>N<sub>0.2</sub>   |               24.63 | Used as a generic “food/biomass” CHON proxy for DEB bookkeeping.          |
| Corn meal (CHO proxy for bookkeeping) |               Yes | starch monomer proxy: C<sub>6</sub>H<sub>10</sub>O<sub>5</sub> |             162.14 | C<sub>1</sub>H<sub>1.667</sub>O<sub>0.833</sub>N<sub>0</sub> |               27.02 | Corn meal appears in Skorupa larval media recipe.                         |
| Agar                                  |                No | (polymer; typically treated inert for nutrition)        |                  — | —                              |                   — | Appears in Skorupa yeast media + larval/mating media recipes.             |
| Tegosept / Nipagin (preservative)     |                No | methyl paraben solution (not nutritionally counted)     |                  — | —                              |                   — | Skorupa uses 20% tegosept; Piper uses nipagin.                            |
| Propionic acid (preservative)         |                No | C<sub>3</sub>H<sub>6</sub>O<sub>2</sub>                 |              74.08 | C<sub>1</sub>H<sub>2</sub>O<sub>0.667</sub>N<sub>0</sub> *(excluded from X<sub>eff</sub>)* |               24.69 | Present in both Skorupa and Piper recipes as preservative.                |
| Amino acids (holidic medium)          |               Yes | mixture (component-specific; see stocks)                |                  — | —                              |                   — | Holidic medium stock solutions list the AA identities and concentrations. |

For each diet (per 1 L = 1000 cm<sup>3</sup>):

1. Total edible mass: sum the edible gram amounts in the recipe.
2. Nutrient mass density: $d_X = (\sum m_i)/1000$ (g·cm<sup>-3</sup>).
3. Weighted carbon mass per C-mol: $w_X = \dfrac{\sum m_i\,w_{C,i}}{\sum m_i}$ (g per C-mol), using the $w_C$ values from the compound table.
4. Nutrient concentration: $X = d_X / w_X$ (C-mol·cm<sup>-3</sup>).
5. Energy per volume: $\Phi_X = \mu_X\,X$ (energy·cm<sup>-3</sup>), where $\mu_X$ is the food energy density you choose.

The X and $\Phi_X$ columns above use steps 2–5 with the listed edible masses; $\Phi_X$ is reported symbolically as $\mu_X$ multiplied by the computed $X$.

| Diet             | Explicit recipe (per 1 L)                                                                                                                                         | Edible components used for X<sub>eff</sub>                 | X<sub>eff</sub> (CHON per C-mol) | X(q=1) (C-mol·cm<sup>-3</sup>) | Φ<sub>X</sub> (energy·cm<sup>-3</sup>) |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------- | ------------------------------: | --------------------------------- |
| **Larval media** | Water(1) 800 ml; Water(2) 200 ml; **Agar 10 g**; **Dextrose 55 g**; **Corn meal 60 g**; **Sucrose 30 g**; **Yeast 25 g**; 20% tegosept 15 ml; propionic acid 3 ml | yeast 25 g + sucrose 30 g + dextrose 55 g + cornmeal 60 g | C<sub>1</sub>H<sub>1.817</sub>O<sub>0.842</sub>N<sub>0.033</sub> | 6.09×10<sup>-3</sup>             | μ<sub>X</sub>·6.09×10<sup>-3</sup> |
| **Mating media** | Water(1) 750 ml; Water(2) 250 ml; **Agar 20 g**; **Sucrose 100 g**; **Yeast 100 g**; 20% tegosept 15 ml; propionic acid 3 ml                                      | yeast 100 g + sucrose 100 g                               | C<sub>1</sub>H<sub>1.815</sub>O<sub>0.693</sub>N<sub>0.107</sub> | 7.53×10<sup>-3</sup>             | μ<sub>X</sub>·7.53×10<sup>-3</sup> |



[1]: https://pubchem.ncbi.nlm.nih.gov/compound/D-Glucose?utm_source=chatgpt.com "D-Glucose | C6H12O6 | CID 5793 - PubChem - NIH"
[2]: https://pubchem.ncbi.nlm.nih.gov/compound/Sucrose?utm_source=chatgpt.com "Sucrose | C12H22O11 | CID 5988 - PubChem - NIH"
[3]: https://pubs.acs.org/doi/10.1021/cr900227t?utm_source=chatgpt.com "First Principles Insight into the α-Glucan Structures of Starch"
[4]: https://www.fishersci.ca/shop/products/agarose-low-eeo-multi-purpose-molecular-biology-grade-fisher-bioreagents-1/p-24089?utm_source=chatgpt.com "Agarose (Low-EEO/Multi-Purpose/Molecular Biology ..."
[5]: https://bionumbers.hms.harvard.edu/bionumber.aspx?id=101801&utm_source=chatgpt.com "Empirical elemental formula for biomass"


## References

- Kaun, K. R., Chakaborty-Chatterjee, M., & Sokolowski, M. B. (2008). Natural variation in plasticity of glucose homeostasis and food intake. *Journal of Experimental Biology*, 211(19), 3160–3166.
- Wosniack, M. E., Hu, N., Gjorgjieva, J., & Berni, J. (2021). Adaptation of Drosophila larva foraging in response to changes in food distribution. *bioRxiv*, 2021.06.21.449222.

### Notes

- **agar** has \(X=0\) because agar is excluded from the nutritious set \(\mathcal N\).
- In this implementation, **quality q** scales only \(d_X\) (numerator) while \(w_X\) is computed at **quality=1** (constant for a given preset).
- The numeric values above depend only on the preset densities and the compound `ww` definitions in the file.
