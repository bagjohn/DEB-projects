# Lb_assumption_in V1-morph

This note documents how using **structural length at birth** \(L_b\) as a **fixed reference size** simplifies the **V1-morph** feeding/assimilation part of a DEB-style larval model, and provides explicit equations (especially involving \(\{ \dot p_{Am}\}\), \(\dot F_m\), \(\{ \dot F_m\}\), \(\dot p_{Xm}\), etc.).

---

## 1) What is \(L_b\) and what is the V1-morph simplification?

- \(L_b\) is the **volumetric structural length at birth** (onset of feeding). In DEB notation this is the cube-root of structural volume at birth:  
  \[
  L_b = V_b^{1/3}
  \]
  and its *scaled* version is \(l_b = L_b/L_m\). (See notation list.) 

- In a **V1-morph**, growth is effectively “one-dimensional” (e.g., elongation-dominated) and, more generally for our purposes, it is convenient to treat the **post-birth larva** as having a **fixed structural scale** when deriving *feeding frequency* (or bite frequency) mappings from DEB ingestion/assimilation. The DEB textbook explicitly discusses V0/V1 morphs as limiting cases of shape and surface/volume relations. 

**Core assumption (V1-morph, minimal feeding map):**
\[
L(t)\approx L_b \quad \text{for the feeding-frequency derivation in V1}
\]
This does **not** claim the larva does not grow; it states that **within this reduced morph** the *feeding/biting mechanics* are derived at a fixed reference size (onset of feeding), postponing ontogenetic scaling to later morphs.

---

## 2) Size scaling of key DEB feeding/assimilation rates

### 2.1 Ingestion (feeding) power and the functional response

The DEB textbook gives the classic hyperbolic functional response for ingestion (in energy/time, “power”): 

\[
\dot p_X = f \, \dot p_{Xm} = f \, \{\dot p_{Xm}\} \, L^2,
\qquad
f=\frac{x}{1+x}, \quad x=\frac{X}{K}
\tag{1}
\]

where:
- \(X\) is food density, \(K\) is the half-saturation coefficient,
- \(\dot p_{Xm}\) is max ingestion power, \(\{\dot p_{Xm}\}\) is **surface-area-specific** max ingestion power,
- \(L\) is volumetric structural length.

**Under the \(L=L_b\) simplification:**
\[
\dot p_X \;\approx\; f \,\{\dot p_{Xm}\}\,L_b^2
\tag{2}
\]

So, for V1, *all* ingestion-power variability is pushed into \(f(X)\) (and temperature corrections, if used), while the geometric factor becomes a constant \(L_b^2\).

---

### 2.2 Filtering/searching (clearance) rate and \(\dot F_m\)

DEB distinguishes a **filtering/searching rate** \(\dot F\) (volume/time) and its maximum \(\dot F_m\). The symbol list explicitly includes these, including the surface-specific form \(\{\dot F_m\}\): 

\[
\dot F \;\le\; \dot F_m,
\qquad
\dot F_m \text{ has units } L^3\,t^{-1},
\qquad
\{\dot F_m\} \text{ has units } L^3\,L^{-2}\,t^{-1}=L\,t^{-1}.
\tag{3}
\]

In surface-area scaling form (consistent with the ingestion scaling in Eq. 1):
\[
\dot F_m(L) = \{\dot F_m\}\,L^2
\tag{4}
\]

**Under the \(L=L_b\) simplification:**
\[
\dot F_m \;\approx\; \{\dot F_m\}\,L_b^2
\tag{5}
\]

This is the key “collapse” used in V1: the searching/clearance capacity becomes a **constant**.

---

### 2.3 Half-saturation coefficient \(K\) from SU/busy-period logic

The DEB textbook derives the hyperbolic response from a “busy period” argument and shows that the half-saturation coefficient can be written as a ratio of a maximum intake rate to a filtering rate (here written in mass-flux terms): 

\[
K = \frac{\dot J_{XAm}}{\dot F},
\tag{6}
\]

where \(\dot J_{XAm}\) is the maximum food intake rate (in moles/time) and \(\dot F\) is the filtering rate (volume/time).

If we use max values \(\dot F=\dot F_m\), then:
\[
K = \frac{\dot J_{XAm}}{\dot F_m}.
\tag{7}
\]

In a V1 implementation with fixed size, \(\dot F_m\) is fixed by Eq. (5), so \(K\) is effectively controlled by the *compound parameters* \(\dot J_{XAm}\) and \(\{\dot F_m\}\) at \(L_b\).

---

## 3) Assimilation and \(\{\dot p_{Am}\}\) under the \(L_b\) simplification

The DEB symbol list defines \(\{\dot p_{Am}\}\) as the **surface-area-specific maximum assimilation rate** (energy/time/area). 

The standard scaling is:
\[
\dot p_{Am}(L) = \{\dot p_{Am}\}\,L^2
\tag{8}
\]

**Under the \(L=L_b\) simplification:**
\[
\dot p_{Am} \;\approx\; \{\dot p_{Am}\}\,L_b^2
\tag{9}
\]

So in V1, the maximum assimilation power is a constant set by \(L_b\) and the DEB parameter \(\{\dot p_{Am}\}\).

> Note (why \(\{\dot p_{Am}\}\) is a “design” parameter): the textbook discusses \(\{\dot p_{Am}\}\) as a primary design parameter linked to maximum size (via \(L_m=\kappa \{\dot p_{Am}\}/[\dot p_M]\)).

---

## 4) Putting it together: a compact V1 feeding/assimilation block at \(L=L_b\)

A clean V1 “feeding block” that exposes the dependence on \(L_b\) is:

### 4.1 Functional response

\[
f(X)=\frac{X}{X+K}
\qquad\text{(equivalent to Eq. 1 with } x=X/K\text{)}
\tag{10}
\]

### 4.2 Max searching / filtering capacity

\[
\dot F_m^{(V1)} \equiv \dot F_m(L_b)=\{\dot F_m\}\,L_b^2
\tag{11}
\]

### 4.3 Ingestion power at size \(L_b\)

\[
\dot p_X^{(V1)}(X)= f(X)\,\dot p_{Xm}(L_b)
= f(X)\,\{\dot p_{Xm}\}\,L_b^2
\tag{12}
\]

### 4.4 Assimilation power at size \(L_b\)

If you explicitly map ingestion to assimilation via an efficiency (often \(\kappa_X\) is used as digestion/assimilation efficiency in practice; see also the DEB data context that lists **kapX** and \(pAi\) / \(pXi\) variables): 

\[
\dot p_A^{(V1)}(X)= \kappa_X \, \dot p_X^{(V1)}(X)
= \kappa_X \, f(X)\,\{\dot p_{Xm}\}\,L_b^2
\tag{13}
\]

and the corresponding maximum assimilation power is:

\[
\dot p_{Am}^{(V1)}=\{\dot p_{Am}\}\,L_b^2.
\tag{14}
\]

(If you instead treat \(\dot p_A\) as directly controlled by \(f\) through \(\dot p_A=f\,\dot p_{Am}\), then combine Eq. 10 and 14:
\[
\dot p_A^{(V1)}(X)= f(X)\,\{\dot p_{Am}\}\,L_b^2.
\tag{15}
\]
)

---

## 5) Why this is useful specifically for feeding-frequency derivations

If your goal is to map DEB ingestion/assimilation (\(\dot p_X\), \(\dot p_A\)) to **observable feeding frequency** (e.g. bites/s, mouth-hook cycles/s), you typically need a mechanical/behavioral conversion such as:

\[
\dot p_X \;\approx\; E_{\text{bite}} \, f_{\text{bite}}
\quad\text{or}\quad
\dot J_X \;\approx\; m_{\text{bite}} \, f_{\text{bite}}
\tag{16}
\]

The \(L=L_b\) simplification makes the DEB side **constant-geometry**, so:

- the dependence on food environment is carried by \(f(X)\),
- the dependence on the individual’s morphology is condensed to \(L_b^2\) multiplying \(\{\dot p_{Xm}\}\), \(\{\dot p_{Am}\}\), \(\{\dot F_m\}\).

That is exactly what you want in V1: a minimal bridge from DEB parameters to feeding frequency, without committing to full growth/instar scaling.

---

## 6) Scope and limitations (what V1 with fixed \(L_b\) does *not* claim)

- It does **not** assert constant size in reality.
- It is a **model-reduction device**: size dependence is postponed to later morphs where \(L(t)\) is explicitly simulated and \(\dot F_m(L)\), \(\dot p_{Am}(L)\) and \(\dot p_{Xm}(L)\) scale with \(L^2\).
- It becomes questionable when you need:
  - instar-specific feeding scaling,
  - diet effects on size-at-birth,
  - fitting growth curves (mass/length vs time).

---

## 7) Quick reference: parameters and units (as used above)

From the DEB symbol list: 

- \(L_b\): volumetric structural length at birth \([L]\)
- \(\dot F_m\): maximum searching/filtering rate \([L^3\,t^{-1}]\)
- \(\{\dot F_m\}\): surface-specific searching rate \([L\,t^{-1}]\)
- \(\{\dot p_{Am}\}\): surface-specific max assimilation power \([E\,L^{-2}\,t^{-1}]\)
- \(\{\dot p_{Xm}\}\): surface-specific max ingestion power \([E\,L^{-2}\,t^{-1}]\)
- \(K\): half-saturation coefficient (food density units, depends on how \(X\) is measured)
- \(f\): scaled functional response (dimensionless)

---

### Minimal “V1 at birth” summary (single block)

\[
\boxed{
\begin{aligned}
&L(t)\approx L_b\\[2mm]
&f(X)=\frac{X}{X+K}\\[2mm]
&\dot F_m^{(V1)}=\{\dot F_m\}L_b^2\\[2mm]
&\dot p_X^{(V1)}(X)= f(X)\{\dot p_{Xm}\}L_b^2\\[2mm]
&\dot p_A^{(V1)}(X)= f(X)\{\dot p_{Am}\}L_b^2
\end{aligned}}
\tag{17}
\]

