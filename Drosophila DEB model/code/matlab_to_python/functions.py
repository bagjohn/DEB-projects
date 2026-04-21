"""Shared utility functions for DEB conversions."""

from typing import Any
import warnings

import numpy as np

__all__ = ["length", "beta0"]


def length(obj: Any) -> int:
    """LENGTH  Length of vector

    LENGTH(obj) returns max(size(obj)) for non-empty arrays and 0 for
    empty arrays.

    Copyright 2020-2021 The MathWorks, Inc.
    """
    if obj is None:
        return 0

    arr = np.asarray(obj)
    if arr.size == 0:
        return 0
    if arr.ndim == 0:
        return 1
    return int(max(arr.shape))


# Code converted from DEBtool_M\lib\misc\beta0.m
def beta0(x0: Any, x1: Any) -> np.ndarray:
    """beta0
    particular incomplete beta function

    Syntax
    f = beta0(x0, x1)

    Description
    particular incomplete beta function:
      B_x1(4/3,0) - B_x0(4/3,0) = integral_x0^x1 t^(4/3-1) (1-t)^(-1) dt

    Input
    - x0: scalar with lower boundary for integration
    - x1: scalar with upper boundary for integration

    Output
    - f: scalar with particular incomplete beta function

    Remarks
    See also beta_34_0

    Example of use
    beta0(0.1, 0.2)
    """
    x0_arr = np.asarray(x0, dtype=float)
    x1_arr = np.asarray(x1, dtype=float)

    if np.any((x0_arr < 0) | (x0_arr >= 1) | (x1_arr < 0) | (x1_arr >= 1)):
        warnings.warn(
            f"Warning from beta0: argument values ({x0}, {x1}) outside (0,1)"
        )
        return np.array([])
    if np.any(x0_arr > x1_arr):
        warnings.warn(
            f"Warning from beta0: lower boundary {x0} lager than upper boundary {x1}"
        )
        return np.array([])

    n0 = length(x0_arr)
    n1 = length(x1_arr)
    if n0 != n1 and n0 != 1 and n1 != 1:
        warnings.warn(
            f"Warning from beta0: argument values ({x0}, {x1}) outside (0,1)"
        )
        return np.array([])

    x03 = np.power(x0_arr, 1.0 / 3.0).astype(complex)
    x13 = np.power(x1_arr, 1.0 / 3.0).astype(complex)
    a3 = np.sqrt(3.0)

    f1 = (
        -3 * x13
        + a3 * np.arctan((1 + 2 * x13) / a3)
        - np.log(x13 - 1)
        + np.log(1 + x13 + x13**2) / 2
    )
    f0 = (
        -3 * x03
        + a3 * np.arctan((1 + 2 * x03) / a3)
        - np.log(x03 - 1)
        + np.log(1 + x03 + x03**2) / 2
    )
    return f1 - f0
