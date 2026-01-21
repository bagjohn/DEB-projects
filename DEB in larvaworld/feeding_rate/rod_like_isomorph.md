# Appendix B : Larval body as a rod-like cylindrical isomorph

## Scope and assumptions

We treat the larval body as an **isomorph** in the DEB sense: shape is constant during growth, so structural **volume** scales with the cube of structural **length**, and structural **surface area** scales with the square of structural length.

For convenience (and because many larvae are approximately elongated), we represent the body as a **right circular cylinder** with a constant aspect ratio.

## Geometry and DEB mapping

Notation note: we use $L_w$ for observed (physical) length to avoid confusion with the DEB **scaled** length, which is commonly written as $l$.

### Observed (physical) dimensions

Let $L_w$ denote the observed body length (cm) and $R$ the body radius (cm). We approximate **structural volume** $V$ by the geometric cylinder volume

$$
V = \pi R^2 L_w.
$$

The total cylinder surface area (including end caps) is

$$
A_{\mathrm{cyl}} = 2\pi R L_w + 2\pi R^2,
$$

and for elongated larvae ($L_w \gg R$) the lateral area dominates:

$$
A_{\mathrm{cyl}} \approx 2\pi R L_w.
$$

### Constant-shape (isomorph) constraint

We impose a constant aspect ratio

$$
\alpha_{\mathrm{AR}} \equiv \frac{L_w}{R} = \mathrm{const},
$$

so $R = L_w/\alpha_{\mathrm{AR}}$ and therefore

$$
V = \frac{\pi}{\alpha_{\mathrm{AR}}^2}\,L_w^3.
$$

### Structural length and the DEB shape coefficient

In DEB, structural volume and structural length are related by

$$
V = L^3.
$$

For constant shape, observed length $L_w$ is proportional to structural length $L$ via the **shape coefficient** $\delta_M$ (dimensionless):

$$
L = \delta_M\,L_w.
$$

For the cylindrical rod with constant aspect ratio $\alpha_{\mathrm{AR}}$, combining $V=L^3$ with $V=(\pi/\alpha_{\mathrm{AR}}^2)L_w^3$ gives

$$
\delta_M = \left(\frac{\pi}{\alpha_{\mathrm{AR}}^2}\right)^{1/3}.
$$

Equivalently,

$$
L_w = \frac{L}{\delta_M} = \left(\frac{\alpha_{\mathrm{AR}}^2}{\pi}\right)^{1/3} L.
$$

## Implications for DEB flux scaling

For an isomorph, DEB writes size dependence using structural length $L$ with $V=L^3$ and (implicitly) structural surface area proportional to $L^2$. Below are the basic relations used in analyses.

### Surface-area controlled fluxes and capacities ($\propto L^2$)

Assimilation power (energy/time) is written with the surface-area-specific maximum $\{p_{Am}\}$:

$$
\dot p_A = f\,\dot p_{Am} = f\,\{p_{Am}\}\,L^2.
$$

Maximum assimilation power at size $L$ is

$$
\dot p_{Am} = \{p_{Am}\}\,L^2.
$$

For feeding derived from searching/filtering (Chapter 2.1.4), the maximum searching rate scales as

$$
\dot F_m = \{\dot F_m\}\,L^2,
$$

and the maximum ingestion flux of food (amount/time) is

$$
\dot J_{X m} = \{\dot J_{X m}\}\,L^2.
$$

With food density $X$ and half-saturation coefficient $K$, the (hyperbolic) functional response is

$$
f = \frac{X}{K+X},
$$

and ingestion follows

$$
\dot J_X = f\,\dot J_{X m} = f\,\{\dot J_{X m}\}\,L^2.
$$

The DEB textbook link between $K$, searching, and maximum ingestion is

$$
K = \frac{\dot J_{X m}}{\dot F_m} = \frac{\{\dot J_{X m}\}}{\{\dot F_m\}}.
$$

### Volume-controlled costs ($\propto L^3$)

Somatic maintenance power is written using the volume-specific maintenance rate $[p_M]$:

$$
\dot p_M = [p_M] L^3.
$$




