"""
This module provides math helper functions for interpolation, clamping, remapping, angle conversion, and float comparison.

Part of the vectra library. These operate on plain numbers, not any vectra class.
"""

import math

def lerp(start: float, end: float, t: float) -> float:
    """
    Linear interpolation between two numbers.

    Args:
        start: Value at t=0.
        end: Value at t=1.
        t: The interpolation factor.

    Returns:
        The interpolated value.

    >>> lerp(0, 10, 0.5)
    5.0
    """
    return start + (end - start) * t

def clamp(value: float, minimum: float, maximum: float) -> float:
    """
    Restrict a value to a given range.

    Args:
        value: The value to clamp.
        minimum: Lower bound.
        maximum: Upper bound.

    Returns:
        value, or the nearest bound if value falls outside [minimum, maximum].

    >>> clamp(15, 0, 10)
    10
    >>> clamp(-5, 0, 10)
    0
    """
    return max(minimum, min(value, maximum))

def remap(
    value: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float
) -> float:
    """
    Map a value from one range to another.

    Args:
        value: The value to remap.
        old_min: Lower bound of the original range.
        old_max: Upper bound of the original range.
        new_min: Lower bound of the target range.
        new_max: Upper bound of the target range.

    Returns:
        value, rescaled into the new range.

    Raises:
        ZeroDivisionError: If old_min equals old_max.

    >>> remap(5, 0, 10, 0, 100)
    50.0
    """
    t = (value - old_min) / (old_max - old_min)
    return lerp(new_min, new_max, t)

def radians_to_degrees(radians: float) -> float:
    """
    Convert radians to degrees.

    Args:
        radians: Angle in radians.

    Returns:
        Angle in degrees.

    >>> round(radians_to_degrees(math.pi), 2)
    180.0
    """
    return math.degrees(radians)

def degrees_to_radians(degrees: float) -> float:
    """
    Convert degrees to radians.

    Args:
        degrees: Angle in degrees.

    Returns:
        Angle in radians.

    >>> round(degrees_to_radians(180), 2)
    3.14
    """
    return math.radians(degrees)

def approx_equal(a: float, b: float, epsilon: float = 1e-9) -> bool:
    """
    Check if two floats are equal within a small tolerance.

    Args:
        a: First value.
        b: Second value.
        epsilon: Tolerance for comparison.

    Returns:
        True if the values are close, False otherwise.

    >>> approx_equal(0.1 + 0.2, 0.3)
    True
    """
    return abs(a - b) < epsilon