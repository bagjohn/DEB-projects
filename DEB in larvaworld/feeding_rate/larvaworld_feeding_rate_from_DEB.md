# larvaworld_feeding_rate_from_DEB

This document derives (line-by-line) the equations used in **Larvaworld** to compute the **feeding frequency** for the **V1-morph** larva from DEB parameters.

Source code: `larvaworld/lib/model/deb/...` as provided in the pasted file. fileciteturn11file0

## 1. What is meant by “V1-morph” here

In this implementation, larval feeding-related surface-area–specific DEB rates are converted to **volume-specific** rates by dividing by the **birth length** \(L_b\) (a fixed length scale predicted from embryo stage):

- `p_Amm_dt  = p_Am  / Lb * dt`   (volume-specific max assimilation, time-scaled)

- `J_X_Amm_dt = J_X_Am / Lb * dt` (volume-specific max ingestion, time-scaled)

This is the V1-morph scaling used by the model: a fixed \(L_b\) turns area-specific rates into volume-specific rates.

## 2. Inputs and state variables

### 2.1 Substrate nutrient concentration

The substrate object provides a nutrient concentration \(X\) (stored as `substrate.X`). In Larvaworld this is computed from substrate composition and quality (see `composition.py`).

- \(X\): nutrient concentration in the environment (model units, treated as “mol·cm⁻³” equivalent)

- \(q\in[0,1]\): substrate quality (dimensionless), which scales nutrient availability in the substrate module

### 2.2 DEB parameters used in the feeding-rate computation

| symbol (code) | meaning | units in code docs |
|---|---|---|

| \(F_m\) (`F_m`) | maximum surface-area specific searching rate | \(\mathrm{L\,cm^{-2}\,d^{-1}}\) |

| \(p_{Am}\) (`p_Am`) | maximum surface-area specific assimilation rate | \(\mathrm{J\,cm^{-2}\,d^{-1}}\) |

| \(\mu_E\) (`mu_E`) | chemical potential of reserve | \(\mathrm{J\,mol^{-1}}\) |

| \(y_{E X}\) (`y_E_X`) | yield coefficient coupling reserve flux to food flux | dimensionless |

| \(T_A\), \(T_{ref}\), \(T\) | Arrhenius parameters and temperature | K |

| \(V_{bite}\) (`V_bite`) | bite-size: fraction of body volume ingested per feeding motion | dimensionless |

| \(L_b\) (`Lb`) | birth length (V1-morph scale) | cm |


## 3. Derived DEB feeding parameters in the code

The model derives ingestion-related parameters in `derive_pars()`.


### 3.1 Max reserve assimilation flux per area

Code: `J_E_Am = p_Am / mu_E`


$$
\boxed{\{\dot J_{EAm}\} = \frac{p_{Am}}{\mu_E}}
$$

Units: \(\mathrm{mol\,cm^{-2}\,d^{-1}}\).


### 3.2 Max food ingestion flux per area

Code: `J_X_Am = J_E_Am / y_E_X`


$$
\boxed{\{\dot J_{XAm}\} = \frac{\{\dot J_{EAm}\}}{y_{E X}} = \frac{p_{Am}}{\mu_E\,y_{E X}}}
$$

Units: \(\mathrm{mol\,cm^{-2}\,d^{-1}}\).


### 3.3 Half-saturation coefficient

Code: `K = J_X_Am / F_m`


$$
\boxed{K = \frac{\{\dot J_{XAm}\}}{F_m}}
$$

Units: same as \(X\) (model’s nutrient concentration units).


## 4. V1-morph volume-specific filtering rate used by Larvaworld

The DEB_basic property `F` is documented as: “Vol specific filtering rate (cm³/(d·cm³)) = vol(env)/vol(individual)/day”.


Code:

```text
F = J_X_Am * F_m / ( Lb * ( J_X_Am + X * F_m ) )
```

Equation:

$$
\boxed{
F(X)
=
\frac{\{\dot J_{XAm}\}\,F_m}{L_b\,\big(\{\dot J_{XAm}\}+X\,F_m\big)}
}
$$

Units: \([F]=\mathrm{d^{-1}}\).


## 5. Feeding frequency `fr_feed` (Hz)

Code:

```text
freq = F / V_bite * T_factor
freq /= 24*60*60
```

### 5.1 Arrhenius temperature correction

Code: `T_factor = exp(T_A/T_ref - T_A/T)`


$$
\boxed{T_{\mathrm{factor}} = \exp\!\left(\frac{T_A}{T_{ref}} - \frac{T_A}{T}\right)}
$$

Dimensionless.


### 5.2 Feeding frequency in motions·s⁻¹ (Hz)

Assuming \(V_{bite}\) is the fraction of body volume ingested per feeding motion:

$$
\boxed{
fr_{feed}
=
\frac{F(X)}{V_{bite}}\,T_{\mathrm{factor}}\,\frac{1}{86400}
}
$$

Units: \([fr_{feed}] = \mathrm{s^{-1}}\) (Hz).


## 6. Full computation pipeline (minimal)

Given \((p_{Am},\mu_E,y_{E X},F_m,L_b,V_{bite})\), substrate \(X\), and temperature \((T,T_{ref},T_A)\):


1. \(\{\dot J_{XAm}\} = p_{Am}/(\mu_E\,y_{E X})\)

2. \(F(X)= \{\dot J_{XAm}\}F_m / \left[L_b(\{\dot J_{XAm}\}+X F_m)\right]\)

3. \(T_{\mathrm{factor}}=\exp(T_A/T_{ref}-T_A/T)\)

4. \(fr_{feed}= (F/V_{bite})\,T_{\mathrm{factor}}/86400\)  (Hz)


## 7. Notes / pitfalls

- This is a **V1-morph convention**: dividing by \(L_b\) makes the rate volume-specific. Changing \(L_b\) rescales \(F\) and \(fr_{feed}\) by \(1/L_b\).

- In DEB notation, a *dotted* clearance \(\dot F\) (cm³·d⁻¹) relates to this implementation’s volume-specific \(F\) by \(F=\dot F/V\).

- The model uses `substrate.X` directly in \(F(X)\); the *functional response* \(f=X/(K+X)\) is also available (`substrate.get_f(K)`), but the `fr_feed` estimate uses \(F(X)\) as written above.
