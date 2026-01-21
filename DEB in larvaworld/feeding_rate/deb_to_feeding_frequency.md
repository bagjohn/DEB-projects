# From DEB feeding parameters to feeding frequency

This note shows two equivalent pipelines—starting from either **ingestion capacity** or **searching/filtering capacity**—to obtain a **feeding motion frequency** (Hz), assuming each feeding motion ingests a fixed fraction of body volume.

Key DEB references are from Kooijman (2010), Chapter 2.1.4, where the hyperbolic functional response is derived from searching (filtering) and handling times. 

## 0) Symbols and unit conventions

### Food in the environment

- $X$: food density (amount of food per environmental volume). Typical units: **C-mol·cm⁻³** (DEB) or any consistent mass/amount per volume.
- $K$: half-saturation coefficient (same units as $X$); defined by $f=1/2$ when $X=K$.
- $x = X/K$: scaled food density (dimensionless).

### Size

- $L$: structural (volumetric) length (cm). For isomorphs, surface area scales as $L^2$ and volume scales as $L^3$.

### Ingestion (food flux)

- $\dot J_{X A}$: **ingestion flux** of food (amount·time⁻¹), e.g. C-mol·d⁻¹.
- $\{\dot J_{X A m}\}$: **surface-area-specific maximum ingestion rate** (amount·area⁻¹·time⁻¹), e.g. C-mol·cm⁻²·d⁻¹.
- $\dot J_{X A m} = \{\dot J_{X A m}\} L^2$: maximum ingestion flux at size $L$.

### Searching / filtering

- $\dot F$: **filtering/searching rate** (environmental volume·time⁻¹), e.g. cm³·d⁻¹.
- $\{\dot F_m\}$: **specific maximum searching (filtering) rate** (volume·area⁻¹·time⁻¹), e.g. cm³·cm⁻²·d⁻¹ = cm·d⁻¹.
- $\dot F_m = \{\dot F_m\} L^2$: maximum searching rate at size $L$.

### Functional response

- $f$: scaled functional response (dimensionless), mapping food density to ingestion rate.



## 1) Core DEB feeding equations



DEB uses the Holling type-II / Michaelis–Menten form:

$$
f = \frac{x}{1+x} = \frac{X}{K+X}\qquad (1)
$$


In DEB, ingestion scales with surface area:

$$
\dot J_{X A} = f\,\dot J_{X A m} = f\,\{\dot J_{X A m}\} L^2\qquad (2)
$$


Kooijman derives the hyperbola from alternating **searching (binding)** and **handling/processing** periods, yielding a mechanistic link between $K$, searching, and max ingestion: 

$$
K = \frac{\dot J_{X A m}}{\dot F_m}\qquad (3)
$$

Equivalently, using size-specific maxima:

$$
K = \frac{\{\dot J_{X A m}\}}{\{\dot F_m\}}\qquad (4)
$$

This is why DEB treats $\{\dot F_m\}$ as a primary parameter rather than $K$ in many contexts.

## 2) Clearance-rate form: ingestion as “food density × filtered volume”

Given food density $X$ (amount per environmental volume), ingesting by filtering $\dot F$ implies:

$$
\dot J_{X A} = X\,\dot F\qquad (5)
$$

Units check: (amount·vol⁻¹)·(vol·time⁻¹) = amount·time⁻¹.


Combining with the functional response, you can express the **effective filtering rate** as:

$$
\dot F = \frac{\dot J_{X A}}{X} = \frac{f\,\dot J_{X A m}}{X}\qquad (6)
$$

## 3) Pipeline to feeding frequency

You want a **feeding motion frequency** (Hz) given an assumed **bite volume**.

Assumption: each feeding motion ingests a constant fraction $V_{\mathrm{bite}}$ of body volume $V$:

$$
V_{\mathrm{bite}} = \kappa_{\mathrm{bite}}\,V\qquad (7)
$$

where $\kappa_{\mathrm{bite}}$ is dimensionless and $V_{\mathrm{bite}}$ has units of volume.


1. Compute functional response using Eq. (1).

2. Compute ingestion flux using Eq. (2).

3. Convert ingestion flux to **environmental volume cleared per time**:

$$
\dot F = \frac{\dot J_{XA}}{X}\qquad (8)
$$

4. Convert clearance to feeding frequency using the bite volume:

$$
f_{\mathrm{feed}}\;[\mathrm{Hz}] = \frac{\dot F}{\kappa_{\mathrm{bite}}\,V}\;\frac{1}{86400}\qquad (9)
$$

If you work in **days** for $\dot F$, the last factor converts d⁻¹ to s⁻¹.





## 4) Parameter definitions (quick reference)

| symbol | meaning | units |
|---|---|---|
| $X$ | food density in environment | amount·vol⁻¹ (e.g. C-mol·cm⁻³) |
| $K$ | half-saturation coefficient | same as $X$ |
| $f$ | scaled functional response | dimensionless |
| $L$ | structural length | cm |
| $V$ | body volume (isomorph) | cm³ |
| $\{\dot J_{XAm}\}$ | surface-area-specific max ingestion rate | amount·cm⁻²·time⁻¹ |
| $\dot J_{XAm}$ | max ingestion flux at size $L$ | amount·time⁻¹ |
| $\{\dot F_m\}$ | specific max searching/filtering rate | cm³·cm⁻²·time⁻¹ (= cm·time⁻¹) |
| $\dot F$ | effective filtering/clearance rate | cm³·time⁻¹ |
| $\kappa_{\mathrm{bite}}$ | bite volume fraction of body volume per motion | dimensionless |
| $f_{\mathrm{feed}}$ | feeding frequency (motions·s⁻¹) | Hz |
