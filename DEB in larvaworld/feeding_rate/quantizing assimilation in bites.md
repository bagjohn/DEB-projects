# Quantizing assimilation into identical bites (DEB-consistent)

This note formalizes a **bite-quantized** representation of feeding that is *consistent with standard DEB flux notation*: we keep the usual continuous DEB assimilation power \(\dot p_A\) but represent it as a train of identical intake events ("bites", "sips", "mouthfuls").

---

## 1) Start agnostically: define bite volume and food concentration

Let a single bite remove a **fixed volume** of food medium:

- \(V_{\text{bite}}\) — *bite volume* \([\mathrm{cm^3\,bite^{-1}}]\)

Let the food in the medium be described as a DEB substrate concentration:

- \(X\) — *food concentration in medium* \([\mathrm{Cmol\,cm^{-3}}]\)

Then the amount of food (in C-moles) per bite is

\[
\Delta X_{\text{bite}} = X\,V_{\text{bite}}
\qquad [\mathrm{Cmol\,bite^{-1}}].
\]

---

## 2) Reach energy per bite via chemical potential

Let

- \(\mu_X\) — *chemical potential of food* \([\mathrm{J\,Cmol^{-1}}]\)

Then the **energy content of one bite** is

\[
E_{\text{bite}} = \mu_X\,\Delta X_{\text{bite}}
= \mu_X\,X\,V_{\text{bite}}
\qquad [\mathrm{J\,bite^{-1}}].
\]

> Interpretation: \(E_{\text{bite}}\) is the energetic intake associated with one identical bite, given \(X\), \(\mu_X\), and \(V_{\text{bite}}\).

---

## 3) Define a bite frequency and derive it from DEB assimilation

Let \(N(t)\) be the cumulative number of bites. Define the **feeding/bite frequency**

- \(f_{\text{feed}}(t) \equiv \dot N(t)\) — \([\mathrm{bite\,time^{-1}}]\) (e.g. \([\mathrm{s^{-1}}]\) or \([\mathrm{d^{-1}}]\))

DEB gives a continuous **assimilation power**

- \(\dot p_A(t)\) — \([\mathrm{J\,time^{-1}}]\)

Quantization assumption: total assimilation is the sum of bite energies per time:

\[
\dot p_A(t) = f_{\text{feed}}(t)\,E_{\text{bite}}(t).
\]

Therefore, the bite frequency is

\[
\boxed{
f_{\text{feed}}(t)
=
\frac{\dot p_A(t)}{E_{\text{bite}}(t)}
=
\frac{\dot p_A(t)}{\mu_X\,X(t)\,V_{\text{bite}}(t)}
}
\qquad [\mathrm{bite\,time^{-1}}].
\]

### Deterministic vs stochastic bites (optional)
- **Deterministic:** \(N(t)\) increases smoothly with \(\dot N=f_{\text{feed}}\).
- **Stochastic (often realistic):** bites arrive as a Poisson process with intensity \(\lambda(t)=f_{\text{feed}}(t)\).  
  The mean still satisfies \(\mathbb{E}[\dot p_A]=\lambda E_{\text{bite}}\).

---

## 4) Substitute a standard DEB expression for \(\dot p_A\)

A common DEB form is

\[
\dot p_A(t) = f(t)\,\{\dot p_{Am}\}\,S_A(t),
\]

where
- \(f(t)\) — functional response (0–1)
- \(\{\dot p_{Am}\}\) — max surface-area specific assimilation \([\mathrm{J\,time^{-1}\,cm^{-2}}]\)
- \(S_A(t)\) — assimilation surface area \([\mathrm{cm^2}]\)

Then

\[
\boxed{
f_{\text{feed}}(t)
=
\frac{f(t)\,\{\dot p_{Am}\}\,S_A(t)}{\mu_X\,X(t)\,V_{\text{bite}}(t)}
}.
\]

This is the key bridge:
- DEB determines \(\dot p_A\),
- bite energetics determines \(E_{\text{bite}}\),
- their ratio determines \(f_{\text{feed}}\).

---

## 5) Adopt the rod-shape isomorph choice (shape correction included)

For your **rod-shaped isomorph** with a **shape correction** \(\delta_M\), a convenient mapping is to retain DEB’s length-based scaling but correct for shape:

- Structural volume:
\[
V(t) = (\delta_M L(t))^3
\qquad [\mathrm{cm^3}]
\]

- Assimilation area (surface scaling):
\[
S_A(t) = (\delta_M L(t))^2
\qquad [\mathrm{cm^2}]
\]

and thus

\[
\dot p_A(t) = f(t)\,\{\dot p_{Am}\}\,(\delta_M L(t))^2.
\]

So the bite frequency becomes

\[
\boxed{
f_{\text{feed}}(t)
=
\frac{f(t)\,\{\dot p_{Am}\}\,(\delta_M L(t))^2}{\mu_X\,X(t)\,V_{\text{bite}}(t)}
}.
\]

> Note: if you later choose to use an explicit rod lateral area formula (rather than the \((\delta_M L)^2\) isomorph mapping), you can swap \(S_A(t)\) accordingly without changing the rest of the derivation.

---

## 6) The open modeling choice: how should \(V_{\text{bite}}\) scale with size?

At this point, the only missing ingredient is a **growth-dependent** bite volume \(V_{\text{bite}}(t)\), i.e. \(V_{\text{bite}}(L)\).

A general family:

\[
V_{\text{bite}}(L) = \eta\,(\delta_M L)^k
\qquad [\mathrm{cm^3\,bite^{-1}}],
\]

with
- \(\eta\) — prefactor (sets bite magnitude)
- \(k\) — scaling exponent

Two principled options correspond to **area vs volume** scaling:

### (A) Volume-scaled bites: \(k=3\)
\[
V_{\text{bite}}(L)=\eta_V\,V(L)=\eta_V\,(\delta_M L)^3.
\]

**Consequence (for fixed \(X\), \(f\)):**
\[
f_{\text{feed}} \propto \frac{(\delta_M L)^2}{(\delta_M L)^3} \propto L^{-1}.
\]
Larger juveniles take fewer bites per time, but each bite is larger.

### (B) Area-scaled bites: \(k=2\)
\[
V_{\text{bite}}(L)=\eta_S\,(\delta_M L)^2.
\]

**Consequence (for fixed \(X\), \(f\)):**
\[
f_{\text{feed}} \propto \frac{(\delta_M L)^2}{(\delta_M L)^2} \propto L^{0},
\]
so bite frequency tends to remain approximately constant over growth (a “feeding rhythm” interpretation).

---

## 7) Where to decide next

The model is now closed except for the choice of \(V_{\text{bite}}(L)\):

- Do you want a **constant-ish feeding rhythm** across growth?  
  → choose **area scaling** (\(k=2\)).

- Do you want each bite to represent a **fixed fraction of body (structural) volume**?  
  → choose **volume scaling** (\(k=3\)).

Either choice is consistent with the same DEB backbone:
\[
f_{\text{feed}}(t)=\dot p_A(t)/(\mu_X X V_{\text{bite}}).
\]
