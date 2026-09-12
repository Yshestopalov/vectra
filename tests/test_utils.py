"""
Tests for utils.py: lerp, clamp, remap, angle conversion, approx_equal.
"""

import math
import pytest

from vectra.utils import (
    lerp,
    clamp,
    remap,
    radians_to_degrees,
    degrees_to_radians,
    approx_equal,
)


def test_lerp_midpoint():
    assert lerp(0, 10, 0.5) == 5.0


def test_lerp_endpoints():
    assert lerp(0, 10, 0) == 0
    assert lerp(0, 10, 1) == 10


def test_lerp_beyond():
    assert lerp(0, 10, 2) == 20


def test_clamp_within():
    assert clamp(5, 0, 10) == 5


def test_clamp_above():
    assert clamp(15, 0, 10) == 10


def test_clamp_below():
    assert clamp(-5, 0, 10) == 0


def test_remap_basic():
    assert remap(5, 0, 10, 0, 100) == 50.0


def test_remap_zero():
    with pytest.raises(ZeroDivisionError):
        remap(5, 0, 0, 0, 100)


def test_radians_to_degrees():
    assert math.isclose(radians_to_degrees(math.pi), 180.0)


def test_degrees_to_radians():
    assert math.isclose(degrees_to_radians(180), math.pi)


def test_approx_equal_within():
    assert approx_equal(0.1 + 0.2, 0.3)


def test_approx_equal_outside():
    assert not approx_equal(1.0, 1.1)