"""Code converted from DEBtool_M\animal\initial_scaled_reserve.m and DEBtool_M\animal\get_ue0.m"""

from functions import beta0, length
from get_lb import get_lb

__all__ = ["get_ue0", "initial_scaled_reserve"]


def get_ue0(p, eb=1.0, lb0=None):
    """
    get_ue0
    gets initial scaled reserve

    Syntax
    [uE0, lb, info] = get_ue0(p, eb, lb0)

    Description
    Obtains the initial scaled reserve given the scaled reserve density at birth.
    Function get_ue0 does so for eggs, get_ue0_foetus for foetuses.
    Specification of length at birth as third input by-passes its computation,
    so if you want to specify an initial value for this quantity, you should use get_lb directly.

    Input
    - p: 1- or 3-vector with parameters g, k_J / k_M, v_H^b, see get_lb
    - eb: optional scalar with scaled reserve density at birth (default: eb = 1)
    - lb0: optional scalar with scaled length at birth (default: lb obtained from get_lb)

    Output
    - uE0: scaled with scaled reserve at t = 0: U_E^0 g^2 k_M^3 / v^2
      with U_E^0 = M_E^0 / {J_EAm}
    - lb: scalar with scaled length at birth
    - info: indicator equals 1 if successful, 0 otherwise

    Remarks
    See get_ue0_foetus for foetal development.
    See initial_scaled_reserve for a non-dimensionless scaling.

    Example of use
    see mydata_ue0
    """
    if eb is None:
        eb = 1.0  # maximum value as juvenile

    if lb0 is None:
        if len(p) < 3:
            print("not enough input parameters, see get_lb")
            return [], [], 0
        lb, info = get_lb(p, eb)
    else:
        lb = lb0
        info = 1

    # unpack p
    g = p[0]  # energy investment ratio

    xb = g / (eb + g)
    uE0 = (3 * g / (3 * g * xb ** (1.0 / 3.0) / lb - beta0(0, xb))) ** 3

    return uE0, lb, info


def initial_scaled_reserve(f, p, Lb0=None):
    """
    initial_scaled_reserve
    Gets initial scaled reserve

    Syntax
    [U0, Lb, info] = initial_scaled_reserve(f, p, Lb0)

    Description
    Gets initial scaled reserve

    Input
    - f: n-vector with scaled functional responses
    - p: 5-vector with parameters: VHb, g, kJ, kM, v
    - Lb0: optional n-vector with lengths at birth

    Output
    - U0: n-vector with initial scaled reserve: M_E^0 / {J_EAm} or E^0 / {p_Am}
    - Lb: n-vector with length at birth
    - info: n-vector with 1's if successful, 0's otherwise

    Remarks
    Like get_ue0, but allows for vector arguments and
    input and output is not downscaled to dimensionless quantities,

    Example of use
    p = [.8 .42 1.7 1.7 3.24 .012]; initial_scaled_reserve(1, p)
    """
    # unpack parameters
    VHb = p[0]  # d cm^2, scaled maturity at birth: M_H^b/((1-kap){J_EAm})
    g = p[1]    # -, energy investment ratio
    kJ = p[2]   # 1/d, maturity maintenance rate coefficient
    kM = p[3]   # 1/d, somatic maintenance rate coefficient
    v = p[4]    # cm/d, energy conductance

    # if kJ = kM: VHb = g * Lb^3/ v;

    if isinstance(f, (str, bytes)):
        f_list = [f]
    else:
        try:
            f_list = list(f)
        except TypeError:
            f_list = [f]
    nf = len(f_list)
    U0 = [0.0] * nf
    Lb = [0.0] * nf
    info = [0] * nf

    q = [g, kJ / kM, VHb * g ** 2 * kM ** 3 / v ** 2]

    if Lb0 is not None:
        if length(Lb0) == 1:
            try:
                lb0_scalar = list(Lb0)[0]
            except TypeError:
                lb0_scalar = Lb0
            lb0 = [lb0_scalar * kM * g / v] * nf
        else:
            lb0_list = list(Lb0)
            if len(lb0_list) != nf:
                raise ValueError("Lb0 must be a scalar or have the same length as f")
            lb0 = [x * kM * g / v for x in lb0_list]
    else:
        lb0_initial, _ = get_lb(q, f_list[0])
        lb0 = [lb0_initial] * nf  # initial estimate for scaled length

    for i, fi in enumerate(f_list):
        lb, info_i = get_lb(q, fi, lb0[i])
        info[i] = info_i
        # try get_lb1 or get_lb2 for higher accuracy
        Lb[i] = lb * v / kM / g
        uE0, _, _ = get_ue0(q, fi, lb)
        U0[i] = uE0 * v ** 2 / g ** 2 / kM ** 3

    return U0, Lb, info
