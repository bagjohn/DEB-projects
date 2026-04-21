"""Code converted from DEBtool_M\animal\get_lb.m and DEBtool_M\animal\get_lb2.m"""

import warnings
from typing import Callable, Tuple

import numpy as np

from functions import beta0

__all__ = ["get_lb"]


def get_lb(p, eb=1.0, lb0=None):
    """get_lb
    Obtains scaled length at birth, given the scaled reserve density at birth

    Syntax
    [lb, info] = get_lb(p, eb, lb0)

    Description
    Obtains scaled length at birth, given the scaled reserve density at birth.

    Input
    - p: 3-vector with parameters: g, k, v_H^b (see below)
    - eb: optional scalar with scaled reserve density at birth (default eb = 1)
    - lb0: optional scalar with initial estimate for scaled length at birth (default lb0: lb for k = 1)

    Output
    - lb: scalar with scaled length at birth
    - info: indicator equals 1 if successful, 0 otherwise

    Remarks
    The theory behind get_lb, get_tb and get_ue0 is discussed in
      Kooy2009b.
    Solves y(x_b) = y_b for lb with explicit solution for y(x)
      y(x) = x e_H/(1-kap) = x g u_H/ l^3
      and y_b = x_b g u_H^b/ ((1-kap)l_b^3)
      d/dx y = r(x) - y s(x);
      with solution y(x) = v(x) * integral r(x)/ v(x) dx
      and v(x) = exp(- integral s(x) dx).
    A Newton Raphson scheme is used with Euler integration, starting from an
    optional initial value. Replacement of Euler integration by ode23: get_lb1,
    but that function is much lower.
    Shooting method: get_lb2.
    Bisection method (via fzero): get_lb3.
    In case of no convergence, get_lb2 is run automatically as backup.
    Consider the application of get_lb_foetus for an alternative initial value.

    Example of use
    See mydata_ue0
    """
    g = p[0]   # g = [E_G] * v/ kap * {p_Am}, energy investment ratio
    k = p[1]   # k = k_J/ k_M, ratio of maturity and somatic maintenance rate coeff
    vHb = p[2]  # v_H^b = U_H^b g^2 kM^3/ (1 - kap) v^2; U_H^b = M_H^b/ {J_EAm}

    info = 1
    if lb0 is None or _is_empty(lb0):
        lb0 = None

    if k == 1:
        lb = vHb ** (1.0 / 3.0)  # exact solution for k = 1
        return lb, info

    if lb0 is None:
        lb = vHb ** (1.0 / 3.0)  # exact solution for k = 1
    else:
        lb = lb0

    if eb is None or _is_empty(eb):
        eb = 1.0

    n = int(1000 + round(1000 * max(0.0, k - 1.0)))
    xb = g / (g + eb)
    xb3 = xb ** (1.0 / 3.0)
    x = np.linspace(1e-6, xb, n)
    dx = xb / n
    x3 = x ** (1.0 / 3.0)

    b = np.real_if_close(beta0(x, xb), tol=1000) / (3.0 * g)
    t0 = xb * g * vHb
    i = 0
    norm = 1.0
    ni = 100

    while i < ni and norm > 1e-8:
        l = x3 / (xb3 / lb - b)
        s = (k - x) / (1.0 - x) * l / g / x
        v = np.exp(-dx * np.cumsum(s))
        vb = v[-1]
        r = g + l
        rv = r / v
        t = t0 / lb**3 / vb - dx * np.sum(rv)
        dl = xb3 / lb**2 * l**2 / x3
        dlnl = dl / l
        dv = v * np.exp(-dx * np.cumsum(s * dlnl))
        dlnv = dv / v
        dlnvb = dlnv[-1]
        dr = dl
        dlnr = dr / r
        dt = -t0 / lb**3 / vb * (3.0 / lb + dlnvb) - dx * np.sum((dlnr - dlnv) * rv)
        lb = lb - t / dt
        norm = t**2
        i += 1

    if i == ni or lb < 0 or lb > 1 or np.isnan(norm) or np.isnan(lb):
        if lb0 is None:
            lb, info = get_lb2(p, eb)
        elif 0 < lb0 < 1:
            lb, info = get_lb2(p, eb, lb0)
        else:
            lb, info = get_lb2(p, eb)

    if info == 0:
        warnings.warn("warning get_lb: no convergence of l_b")

    return lb, info


def get_lb2(p, eb=1.0, lb0=None):
    """get_lb2
    Obtains scaled length at birth, given the scaled reserve density at birth.

    Like get_lb, but using the shooting method, rather than Newton Raphson.
    """
    g = p[0]
    k = p[1]
    vHb = p[2]

    info = 1
    if lb0 is None or k == 1:
        lb = vHb ** (1.0 / 3.0)
        if k == 1:
            return lb, info
    elif _is_empty(lb0):
        lb = vHb ** (1.0 / 3.0)
    else:
        lb = lb0

    if eb is None or _is_empty(eb):
        eb = 1.0

    xb = g / (eb + g)
    xb3 = xb ** (1.0 / 3.0)

    f0 = _fn_get_lb2(lb, xb, xb3, g, vHb, k)
    if np.isnan(f0):
        return lb, 0

    lb_root, ok = _root_bisect(
        lambda val: _fn_get_lb2(val, xb, xb3, g, vHb, k),
        lb,
        xmin=1e-10,
        xmax=1.0 - 1e-10,
        tol=1e-10,
        max_iter=80,
    )
    info = 1 if ok and 0 < lb_root < 1 and np.isfinite(lb_root) else 0
    return lb_root, info


def _fn_get_lb2(lb: float, xb: float, xb3: float, g: float, vHb: float, k: float) -> float:
    """Residual for get_lb2 shooting method."""
    if lb <= 0:
        return np.nan
    y_end = _integrate_lb2(lb, xb, xb3, g, k)
    return y_end - xb * g * vHb / lb**3


def _integrate_lb2(lb: float, xb: float, xb3: float, g: float, k: float) -> float:
    """Integrate dget_lb2 from x=1e-10 to x=xb with y(0)=0 using RK4."""
    n_steps = 2000
    xs = np.linspace(1e-10, xb, n_steps)
    y = 0.0
    for i in range(n_steps - 1):
        x = xs[i]
        h = xs[i + 1] - x
        k1 = _dget_lb2(x, y, lb, xb, xb3, g, k)
        k2 = _dget_lb2(x + 0.5 * h, y + 0.5 * h * k1, lb, xb, xb3, g, k)
        k3 = _dget_lb2(x + 0.5 * h, y + 0.5 * h * k2, lb, xb, xb3, g, k)
        k4 = _dget_lb2(x + h, y + h * k3, lb, xb, xb3, g, k)
        y += (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


def _dget_lb2(x: float, y: float, lb: float, xb: float, xb3: float, g: float, k: float) -> float:
    """Derivative for get_lb2 shooting method."""
    x3 = x ** (1.0 / 3.0)
    b = np.real_if_close(beta0(x, xb), tol=1000)
    b = float(np.asarray(b).squeeze())
    l = x3 / (xb3 / lb - b / (3.0 * g))
    return l + g - y * (k - x) / (1.0 - x) * l / g / x


def _root_bisect(
    fn: Callable[[float], float],
    x0: float,
    xmin: float,
    xmax: float,
    tol: float = 1e-10,
    max_iter: int = 80,
) -> Tuple[float, bool]:
    """Robust bracket search + bisection to mimic fzero fallback."""
    bracket = _find_bracket(fn, x0, xmin, xmax)
    if bracket is None:
        return x0, False

    a, b, fa, fb = bracket
    if fa == 0:
        return a, True
    if fb == 0:
        return b, True

    for _ in range(max_iter):
        c = 0.5 * (a + b)
        fc = fn(c)
        if np.isnan(fc):
            return c, False
        if abs(fc) < tol or abs(b - a) < tol:
            return c, True
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return 0.5 * (a + b), False


def _find_bracket(
    fn: Callable[[float], float],
    x0: float,
    xmin: float,
    xmax: float,
    max_steps: int = 50,
):
    """Find a sign-changing bracket around x0 within [xmin, xmax]."""
    x0 = min(max(x0, xmin), xmax)
    f0 = fn(x0)
    if np.isnan(f0):
        return None

    step = 0.05
    a = b = x0
    for _ in range(max_steps):
        a = max(xmin, x0 - step)
        b = min(xmax, x0 + step)
        fa = fn(a)
        fb = fn(b)
        if np.isnan(fa) or np.isnan(fb):
            step *= 1.5
            continue
        if fa * fb < 0:
            return a, b, fa, fb
        if a == xmin and b == xmax:
            break
        step *= 1.5
    return None


def _is_empty(value) -> bool:
    if value is None:
        return True
    try:
        return len(value) == 0
    except TypeError:
        return False
