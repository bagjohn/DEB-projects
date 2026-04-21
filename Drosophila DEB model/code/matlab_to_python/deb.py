import json
import math
import os

import param

from initial_scaled_reserve import initial_scaled_reserve
from param import Number, Parameterized, String
from tempcorr import tempcorr

__all__: list[str] = [
    "DEB_model",
    "Drosophila_DEB_model"
    ]


class DEB_model(Parameterized):
    """Base DEB model with parameters defined from JSON symbols.

    This class is intended to be used as a generator for concrete DEB models
    via :meth:`species_specific_DEB_model_from_json`. It should not be
    instantiated directly.
    """

    # Metadata
    species = String(None, allow_None=True, doc='Species identifier')
    typified_model = String(None, allow_None=True, doc='Typified DEB model identifier')

    # Parameters

    # Temperature-related parameters
    T_ref = Number(293.1, doc='Reference temperature (K)')
    T_A = Number(28890.0, doc='Arrhenius temperature (K)')

    # General parameters
    z = Number(None, allow_None=True, doc='zoom factor (-)')
    F_m = Number(None, allow_None=True, doc='{F_m}, max specific searching rate (l/d.cm^2)')
    v = Number(None, allow_None=True, doc='energy conductance (cm/d)')
    E_G = Number(None, allow_None=True, doc='[E_G], specific cost for structure (J/cm^3)')
    kap = Number(None, allow_None=True, doc='allocation fraction to soma (-)')

    # Food quality
    f = Number(1.0, doc='scaled functional response for 0-var data (-)')

    # Efficiency parameters
    kap_R = Number(None, allow_None=True, doc='reproduction efficiency (-)')
    kap_X = Number(None, allow_None=True, doc='digestion efficiency of food to reserve (-)')
    kap_P = Number(None, allow_None=True, doc='faecation efficiency of food to faeces (-)')
    kap_V = Number(None, allow_None=True, doc='conversion efficient E -> V -> E (-)')

    # Maintenance parameters
    p_M = Number(None, allow_None=True, doc='[p_M], vol-specific somatic maintenance (J/d.cm^3)')
    p_T = Number(None, allow_None=True, doc='{p_T}, surf-specific somatic maintenance (J/d.cm^2)')
    k_J = Number(None, allow_None=True, doc='maturity maintenance rate coefficient (1/d)')
    
    
    # Maturity and reproduction buffer checkpoints
    E_Hb = Number(None, allow_None=True, doc='maturity at birth (J)')
    E_Hp = Number(None, allow_None=True, doc='maturity at puberty (J)')
    E_He = Number(None, allow_None=True, doc='maturity at emergence (J)')
    E_Rb = Number(0.0, doc='reproduction buffer at birth (J)')
    E_Rj = Number(0.0, doc='reproduction buffer at puberty (J)')
    E_Re = Number(None, allow_None=True, doc='reproduction buffer at emergence (J)')
    v_Rj = Number(0.0, doc='scaled reproduction buffer at puberty (-)')
    v_Re = Number(None, allow_None=True, doc='scaled reproduction buffer at emergence (-)')



    # Scaled Maturity parameters
    M_Hb = Number(None, allow_None=True, doc='M_Hb, maturity at birth (mmol)')
    U_Hb = Number(None, allow_None=True, doc='U_Hb, scaled maturity at birth (cm^2 d)')
    V_Hb = Number(None, allow_None=True, doc='V_Hb, scaled maturity at birth (cm^2 d)')
    v_Hb = Number(None, allow_None=True, doc='v_Hb, scaled maturity density at birth (-)')
    u_Hb = Number(None, allow_None=True, doc='u_Hb, scaled maturity density at birth (-)')
    M_Hp = Number(None, allow_None=True, doc='M_Hp, maturity at puberty (mmol)')
    U_Hp = Number(None, allow_None=True, doc='U_Hp, scaled maturity at puberty (cm^2 d)')
    V_Hp = Number(None, allow_None=True, doc='V_Hp, scaled maturity at puberty (cm^2 d)')
    v_Hp = Number(None, allow_None=True, doc='v_Hp, scaled maturity density at puberty (-)')
    u_Hp = Number(None, allow_None=True, doc='u_Hp, scaled maturity density at puberty (-)')
    M_He = Number(None, allow_None=True, doc='M_He, maturity at emergence (mmol)')
    U_He = Number(None, allow_None=True, doc='U_He, scaled maturity at emergence (cm^2 d)')
    V_He = Number(None, allow_None=True, doc='V_He, scaled maturity at emergence (cm^2 d)')
    v_He = Number(None, allow_None=True, doc='v_He, scaled maturity density at emergence (-)')
    u_He = Number(None, allow_None=True, doc='u_He, scaled maturity density at emergence (-)')

    # Initial reserve
    E_0 = Number(None, allow_None=True, doc='E_0, initial reserve (J)')

    # Shape parameters
    del_M = Number(None, allow_None=True, doc='shape coefficient for head capsule of larva (-)')
    del_Mw = Number(None, allow_None=True, doc='shape coefficient for wing length of imago (-)')
    s_1 = Number(None, allow_None=True, doc='stress at instar 1: L_1^2/ L_b^2 (-)')
    s_2 = Number(None, allow_None=True, doc='stress at instar 2: L_2^2/ L_1^2 (-)')

    # Aging parameters
    h_a = Number(None, allow_None=True, doc='Weibull aging acceleration (1/d^2)')
    s_G = Number(None, allow_None=True, doc='Gompertz stress coefficient (-)')

    # Derived parameters. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    p_Am = Number(None, allow_None=True, doc='{p_Am} specific assimilation flux (J/d.cm^2); expression includes L_m^ref = 1 cm for unit consistency.')
    E_m = Number(None, allow_None=True, doc='[E_m], reserve capacity (J/cm^3)')
    g = Number(None, allow_None=True, doc='g, energy investment ratio (-)')
    L_m = Number(None, allow_None=True, doc='L_m, maximum length (cm)')
    L_T = Number(None, allow_None=True, doc='L_T, heating length (cm; also applies to osmotic work)')
    l_T = Number(None, allow_None=True, doc='l_T, scaled heating length (-)')
    k_M = Number(None, allow_None=True, doc='k_M, somatic maintenance rate coefficient (1/d)')
    k = Number(None, allow_None=True, doc='k, maintenance ratio (-)')
    s_s = Number(None, allow_None=True, doc='s_s, supply stress (-)')
    
    M_V = Number(None, allow_None=True, doc='[M_V], volume-specific mass of structure (mol/cm^3)')
    y_V_E = Number(None, allow_None=True, doc='y_V_E, yield of structure on reserve (mol/mol)')
    y_E_V = Number(None, allow_None=True, doc='y_E_V, yield of reserve on structure (mol/mol)')
    m_Em = Number(None, allow_None=True, doc='m_Em, reserve capacity (mol/mol)')
    J_E_Am = Number(None, allow_None=True, doc='{J_EAm}, max surface-spec assimilation flux (mol/d.cm^2)')
    K = Number(None, allow_None=True, doc='K, half-saturation coefficient (c-mol X/l)')
    s_H = Number(None, allow_None=True, doc='s_H, precociality index (-)')

    # Yield coefficients. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    y_E_X = Number(None, allow_None=True, doc='y_E_X, yield of reserve on food (mol/mol)')
    y_X_E = Number(None, allow_None=True, doc='y_X_E, yield of food on reserve (mol/mol)')
    y_P_X = Number(None, allow_None=True, doc='y_P_X, yield of faeces on food (mol/mol)')
    y_X_P = Number(None, allow_None=True, doc='y_X_P, yield of food on faeces (mol/mol)')
    y_P_E = Number(None, allow_None=True, doc='y_P_E, yield of faeces on reserve (mol/mol)')
    y_V_E = Number(None, allow_None=True, doc='y_V_E, yield of structure on reserve (mol/mol)')
    y_E_V = Number(None, allow_None=True, doc='y_E_V, yield of reserve on structure (mol/mol)')

    # Feeding powers and fluxes. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    p_Xm = Number(None, allow_None=True, doc='p_Xm, max spec feeding power (J/d.cm^2)')
    J_X_Am = Number(None, allow_None=True, doc='{J_XAm}, max surface-spec feeding flux (mol/d.cm^2)')

    # Energy couplers. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    eta_XA = Number(None, allow_None=True, doc='eta_XA, food-assim energy coupler (mol/J)')
    eta_PA = Number(None, allow_None=True, doc='eta_PA, faeces-assim energy coupler (mol/J)')
    eta_VG = Number(None, allow_None=True, doc='eta_VG, struct-growth energy coupler (mol/J)')

    # Maintenance costs. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    J_E_M = Number(None, allow_None=True, doc='[J_EM], volume-spec somatic maint costs (mol/d.cm^3)')
    J_E_T = Number(None, allow_None=True, doc='{J_ET}, surface-spec somatic maint costs (mol/d.cm^2)')
    j_E_M = Number(None, allow_None=True, doc='j_E_M, mass-spec somatic maint costs (mol/d.mol)')
    j_E_J = Number(None, allow_None=True, doc='j_E_J, mass-spec maturity maint costs (mol/d.mol)')
    kap_G = Number(None, allow_None=True, doc='kap_G, growth efficiency (-)')
    E_V = Number(None, allow_None=True, doc='[E_V], volume-specific energy of structure (J/cm^3)')

    # Molecular weights. Code converted from DEBtool_M\lib\pet\parscomp_st.m
    w_X = Number(None, allow_None=True, doc='w_X, mol-weights for (unhydrated) org. compounds: food (g/mol)')
    w_V = Number(None, allow_None=True, doc='w_V, mol-weights for (unhydrated) org. compounds: structure (g/mol)')
    w_E = Number(None, allow_None=True, doc='w_E, mol-weights for (unhydrated) org. compounds: reserve (g/mol)')
    w_P = Number(None, allow_None=True, doc='w_P, mol-weights for (unhydrated) org. compounds: faeces (g/mol)')


    # Specific densities. Code converted from DEBtool_M\lib\pet\addchem.m
    d_X = Number(None, allow_None=True, doc='d_X, specific density of food (g/cm^3)')
    d_V = Number(None, allow_None=True, doc='d_V, specific density of structure (g/cm^3)')
    d_E = Number(None, allow_None=True, doc='d_E, specific density of reserve (g/cm^3)')
    d_P = Number(None, allow_None=True, doc='d_P, specific density of faeces (g/cm^3)')

    # Chemical potentials from Kooy2010 Tab 4.2. Code converted from DEBtool_M\lib\pet\addchem.m
    mu_X = Number(525000.0, doc='mu_X, chemical potential of food (J/mol)')
    mu_V = Number(500000.0, doc='mu_V, chemical potential of structure (J/mol)')
    mu_E = Number(550000.0, doc='mu_E, chemical potential of reserve (J/mol)')
    mu_P = Number(480000.0, doc='mu_P, chemical potential of faeces (J/mol)')

    # Chemical potentials of minerals. Code converted from DEBtool_M\lib\pet\addchem.m
    mu_C = Number(0.0, doc='mu_C, chemical potential of CO2 (J/mol)')
    mu_H = Number(0.0, doc='mu_H, chemical potential of H2O (J/mol)')
    mu_O = Number(0.0, doc='mu_O, chemical potential of O2 (J/mol)')
    mu_N = Number(None, allow_None=True, doc='mu_N, chemical potential of N-waste (J/mol)')

    # Chemical indices for water-free organics from Kooy2010 Fig 4.15. Code converted from DEBtool_M\lib\pet\addchem.m
    n_CX = Number(1.0, doc='n_CX, chem. index of carbon in food (-)')
    n_HX = Number(1.8, doc='n_HX, chem. index of hydrogen in food (-)')
    n_OX = Number(0.5, doc='n_OX, chem. index of oxygen in food (-)')
    n_NX = Number(0.15, doc='n_NX, chem. index of nitrogen in food (-)')
    n_CV = Number(1.0, doc='n_CV, chem. index of carbon in structure (-)')
    n_HV = Number(1.8, doc='n_HV, chem. index of hydrogen in structure (-)')
    n_OV = Number(0.5, doc='n_OV, chem. index of oxygen in structure (-)')
    n_NV = Number(0.15, doc='n_NV, chem. index of nitrogen in structure (-)')
    n_CE = Number(1.0, doc='n_CE, chem. index of carbon in reserve (-)')
    n_HE = Number(1.8, doc='n_HE, chem. index of hydrogen in reserve (-)')
    n_OE = Number(0.5, doc='n_OE, chem. index of oxygen in reserve (-)')
    n_NE = Number(0.15, doc='n_NE, chem. index of nitrogen in reserve (-)')
    n_CP = Number(1.0, doc='n_CP, chem. index of carbon in faeces (-)')
    n_HP = Number(1.8, doc='n_HP, chem. index of hydrogen in faeces (-)')
    n_OP = Number(0.5, doc='n_OP, chem. index of oxygen in faeces (-)')
    n_NP = Number(0.15, doc='n_NP, chem. index of nitrogen in faeces (-)')

    # Parameters predicted from data via DEBtool optimization
    ab = Number(None, allow_None=True, doc='age at birth (d)')
    t1 = Number(None, allow_None=True, doc='duration of instar 1 (d)')
    t2 = Number(None, allow_None=True, doc='duration of instar 2 (d)')
    tj = Number(None, allow_None=True, doc='time since birth at pupation (d)')
    tje = Number(None, allow_None=True, doc='time since pupation at emergence (d)')
    Lb = Number(None, allow_None=True, doc='physical length of young instar 1 (cm)')
    L1 = Number(None, allow_None=True, doc='physical length at end of instar 1 (cm)')
    L2 = Number(None, allow_None=True, doc='physical length at end of instar 2 (cm)')
    Lj = Number(None, allow_None=True, doc='physical length of pupa (cm)')
    Ri = Number(None, allow_None=True, doc='mean daily fecundity (first 10 d), eggs per female per day (#/d)')

    # State variables
    E = Number(0.0, doc='reserve (J)')
    L = Number(0.0, doc='structural length (cm)')
    EH = Number(0.0, doc='maturity (J)')
    ER = Number(0.0, doc='reproduction buffer (J)')
    V = Number(0.0, doc='structural volume (cm^3); nominally L**3')
    a = Number(0.0, doc='age since oviposition (d)')

    @param.depends("L", watch=True)
    def _sync_V_from_L(self) -> None:
        """Keep V synced to L**3."""
        self.param.set_param(V=self.L ** 3)


    def __init__(self, **params) -> None:
        """Prevent direct instantiation of the base class."""
        if self.__class__ is DEB_model:
            raise TypeError(
                "DEB_model is a generator base class and cannot be instantiated. "
                "Use DEB_model.species_specific_DEB_model_from_json(...) or a concrete subclass."
            )
        super().__init__(**params)
        # Core derived parameters (parscomp_st.m)
        L_m_ref = 1.0  # cm, reference maximum structural length for unit consistency
        self.p_Am = self.z * self.p_M / self.kap * L_m_ref
        self.E_m = self.p_Am / self.v
        self.g = self.E_G / self.kap / self.E_m
        self.k_M = self.p_M / self.E_G
        self.L_m = self.v / self.k_M / self.g
        self.L_T = self.p_T / self.p_M
        self.l_T = self.L_T / self.L_m
        self.k = self.k_J / self.k_M
        self.s_s = self.k_J * self.E_Hp * (self.p_M ** 2) / (self.p_Am ** 3)
        # Precociality index (parscomp_st.m)
        if self.E_Hp is not None and self.E_Hb is not None:
            self.s_H = self.E_Hb / self.E_Hp
        else:
            self.s_H = 1.0
        self._compute_scaled_maturity_levels()
        
        # Chemical indices and molecular weights (parscomp_st.m)
        self.n_O = [
            [self.n_CX, self.n_CV, self.n_CE, self.n_CP],
            [self.n_HX, self.n_HV, self.n_HE, self.n_HP],
            [self.n_OX, self.n_OV, self.n_OE, self.n_OP],
            [self.n_NX, self.n_NV, self.n_NE, self.n_NP],
        ]
        weights = [12.0, 1.0, 16.0, 14.0]
        w_O = [
            sum(self.n_O[row][col] * weights[row] for row in range(4))
            for col in range(4)
        ]
        self.w_X, self.w_V, self.w_E, self.w_P = w_O
        # Flux conversion
        self.J_E_Am = self.p_Am / self.mu_E
        # Yield coefficients and feeding (parscomp_st.m)
        if self.kap_X is not None:
            self.y_E_X = self.kap_X * self.mu_X / self.mu_E
            self.y_X_E = 1.0 / self.y_E_X
            self.p_Xm = self.p_Am / self.kap_X
            self.J_X_Am = self.y_X_E * self.J_E_Am
        if self.kap_P is not None:
            self.y_P_X = self.kap_P * self.mu_X / self.mu_P
            self.y_X_P = 1.0 / self.y_P_X
        if self.kap_X is not None and self.kap_P is not None and self.y_V_E is not None:
            self.y_P_E = self.y_P_X / self.y_E_X
        # Energy couplers (parscomp_st.m)
        if self.kap_X is not None and self.kap_P is not None and self.y_P_E is not None and self.y_V_E is not None:
            self.eta_XA = self.y_X_E / self.mu_E
            self.eta_PA = self.y_P_E / self.mu_E
            self.eta_VG = self.y_V_E / self.mu_E
            self.eta_O = [
                [-self.eta_XA, 0.0, 0.0],
                [0.0, 0.0, self.eta_VG],
                [1.0 / self.mu_E, -1.0 / self.mu_E, -1.0 / self.mu_E],
                [self.eta_PA, 0.0, 0.0],
            ]
        # Maintenance costs and efficiencies (parscomp_st.m)
        self.J_E_M = self.p_M / self.mu_E
        self.J_E_T = self.p_T / self.mu_E
        self.j_E_M = self.k_M * self.y_E_V if self.y_E_V is not None else None
        self.j_E_J = self.k_J * self.y_E_V if self.y_E_V is not None else None
        if self.d_V is not None:
            # Structure density-dependent conversions (addchem.m + parscomp_st.m)
            if self.d_X is None:
                self.d_X = self.d_V
            if self.d_E is None:
                self.d_E = self.d_V
            if self.d_P is None:
                self.d_P = self.d_V
            self.M_V = self.d_V / self.w_V
            self.y_V_E = self.mu_E * self.M_V / self.E_G
            self.y_E_V = 1.0 / self.y_V_E
            self.m_Em = self.y_E_V * self.E_m / self.E_G
            self.kap_G = self.mu_V * self.M_V / self.E_G
            self.E_V = self.d_V * self.mu_V / self.w_V
        # Half-saturation and pupation buffer (parscomp_st.m)
        if self.F_m is not None and self.J_X_Am is not None:
            self.K = self.J_X_Am / self.F_m
        # Scaled reproduction buffer at pupation and emergence (parscomp_st.m)
        if self.E_Rj is not None:
            self.v_Rj = self.kap / (1.0 - self.kap) * self.E_Rj / self.E_G
        #if self.E_Re is not None:
        #    self.v_Re = self.kap / (1.0 - self.kap) * self.E_Re / self.E_G

        # Life stages

        # Initial
        self._compute_initial_reserve()

        


    def _compute_scaled_maturity_levels(self) -> None:
        """Compute scaled maturity levels (parscomp_st.m)."""
        if (
            self.mu_E is None
            or self.p_Am is None
            or self.kap is None
            or self.g is None
            or self.k_M is None
            or self.v is None
        ):
            return
        maturity_levels = {
            "b": self.E_Hb,
            "p": self.E_Hp,
            "e": self.E_He,
        }
        for suffix, E_H in maturity_levels.items():
            if E_H is None:
                continue
            M_H = E_H / self.mu_E
            U_H = E_H / self.p_Am
            V_H = U_H / (1.0 - self.kap)
            v_H = V_H * self.g ** 2 * self.k_M ** 3 / self.v ** 2
            u_H = U_H * self.g ** 2 * self.k_M ** 3 / self.v ** 2
            setattr(self, f"M_H{suffix}", M_H)
            setattr(self, f"U_H{suffix}", U_H)
            setattr(self, f"V_H{suffix}", V_H)
            setattr(self, f"v_H{suffix}", v_H)
            setattr(self, f"u_H{suffix}", u_H)

    def _compute_initial_reserve(self) -> None:
        """Compute initial reserve E_0 from scaled maturity (parscomp_st.m)."""
        if (
            self.V_Hb is None
            or self.g is None
            or self.k_J is None
            or self.k_M is None
            or self.v is None
            or self.f is None
            or self.p_Am is None
        ):
            return
        pars_UE0 = [self.V_Hb, self.g, self.k_J, self.k_M, self.v]
        U_E0, _Lb, _info = initial_scaled_reserve([self.f], pars_UE0)
        self.E_0 = self.p_Am * U_E0[0]

    def _tempcorr(self, T: float | None = None):
        """Return temperature correction factor at T (defaults to T_ref)."""
        if T is None:
            T = self.T_ref
        return tempcorr(T=T, T_ref=self.T_ref, pars_T=self.T_A)

    def get_state_variables(self) -> dict[str, float | None]:
        """Return current state variables as a dict."""
        return {
            "E": self.E,
            "L": self.L,
            "EH": self.EH,
            "ER": self.ER,
        }

    def dget_ELH_larva(self, f: float | None = None, T: float | None = None):
        """Larval development ODE: returns [dE, dL, dEH] at current state."""
        if f is None:
            f = self.f
        TC = self._tempcorr(T)

        E = self.E
        L = self.L
        EH = self.EH
        V = L ** 3

        pT_M = TC * self.p_M
        pT_Am = TC * self.p_Am
        kT_J = TC * self.k_J
        vT = TC * self.v

        s_M = L / self.Lb

        r = (E * vT * s_M / L - pT_M * V / self.kap) / (E + self.E_G * V / self.kap)
        p_C = E * (self.E_G * vT * s_M / L + pT_M) / (self.kap * E / V + self.E_G)

        dE = f * pT_Am * s_M * L ** 2 - p_C
        dL = r * L / 3 * (L < self.Lj)
        dEH = (1 - self.kap) * p_C - kT_J * EH

        return [dE, dL, dEH]

    def dget_ELHE_imago(
        self, f: float | None = None, T: float | None = None
    ):
        """Imago ODE: returns [dE, dL, dEH, dER] at current state."""
        if f is None:
            f = self.f
        TC = self._tempcorr(T)

        E = self.E
        L = self.L
        EH = self.EH
        ER = self.ER

        pT_Am = TC * self.p_Am
        kT_J = TC * self.k_J
        vT = TC * self.v

        s_M = self.Lj / self.Lb
        pC = E * vT * s_M / L

        dE = f * pT_Am * L ** 2 * s_M - pC
        dL = 0.0
        dEH = 0.0
        dER = (1 - self.kap) * pC - kT_J * EH

        return [dE, dL, dEH, dER]

    @classmethod
    def species_specific_DEB_model_from_json(
        cls, json_path: str, class_name: str | None = None
    ) -> "type[DEB_model]":
        """Generate a new Parameterized subclass using defaults from a JSON file."""
        with open(json_path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)

        metadata = payload.get("metadata", {})
        parameters = payload.get("parameters", [])
        data_predictions = payload.get("data_predictions", [])

        species_value = metadata.get("species")
        typified_value = metadata.get("typified_model")
        if not species_value or not typified_value:
            raise ValueError(
                "metadata must include non-empty 'species' and 'typified_model' values."
            )

        if class_name is None:
            raw_name = species_value
            sanitized = "".join(ch if ch.isalnum() else "_" for ch in raw_name)
            class_name = sanitized if sanitized and sanitized[0].isalpha() else f"DEBModel_{sanitized}"

        attributes: dict[str, object] = {"__doc__": species_value}

        model_cls = type(class_name, (cls,), attributes)

        for entry in parameters:
            symbol = entry.get("symbol")
            value = entry.get("value")
            if symbol in model_cls.param:
                model_cls.param[symbol].default = value
                if value:
                    model_cls.param[symbol].allow_None = False

        for entry in data_predictions:
            symbol = entry.get("symbol")
            prd_value = entry.get("prd")
            if symbol in model_cls.param and prd_value is not None:
                model_cls.param[symbol].default = prd_value
                model_cls.param[symbol].allow_None = False

        model_cls.param["species"].default = species_value
        model_cls.param["typified_model"].default = typified_value

        return model_cls


DROSOPHILA_DEB_JSON_PATH = os.path.join(
    os.path.dirname(__file__), "Drosophila_melanogaster_DEB_pars.json"
)

Drosophila_DEB_model = DEB_model.species_specific_DEB_model_from_json(
    DROSOPHILA_DEB_JSON_PATH, class_name="Drosophila_DEB_model"
)
Drosophila_DEB_model.param["d_V"].default = 0.17 # from get_d_V('Arthropoda', 'Insecta') in DEBtool_M\lib\pet\get_d_V.m
Drosophila_DEB_model.param["d_V"].allow_None = False  
