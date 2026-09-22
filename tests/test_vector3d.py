"""
Tests for the Vector3D class.
"""

import pytest

from vectra import Vector3D


def test_init():
    v = Vector3D(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3


def test_repr():
    assert repr(Vector3D(1, 2, 3)) == "Vector3D(1, 2, 3)"


def test_eq_same():
    assert Vector3D(1, 2, 3) == Vector3D(1, 2, 3)


def test_eq_different():
    assert Vector3D(1, 2, 3) != Vector3D(4, 5, 6)


def test_eq_non_vector():
    assert Vector3D(1, 2, 3) != 5
    assert Vector3D(1, 2, 3) != "1, 2, 3"


def test_unhashable():
    with pytest.raises(TypeError):
        hash(Vector3D(1, 2, 3))


def test_add():
    assert Vector3D(1, 2, 3) + Vector3D(4, 5, 6) == Vector3D(5, 7, 9)


def test_add_non_vector():
    with pytest.raises(TypeError):
        Vector3D(1, 2, 3) + 5


def test_add_string():
    with pytest.raises(TypeError):
        "abc" + Vector3D(1, 2, 3)


def test_add_new_instance():
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    result = a + b

    assert result is not a
    assert result is not b


def test_sub():
    assert Vector3D(5, 7, 9) - Vector3D(4, 5, 6) == Vector3D(1, 2, 3)


def test_sub_non_vector():
    with pytest.raises(TypeError):
        Vector3D(1, 2, 3) - 5


def test_sub_string():
    with pytest.raises(TypeError):
        "abc" - Vector3D(1, 2, 3)


def test_sub_new_instance():
    a = Vector3D(5, 7, 9)
    b = Vector3D(4, 5, 6)
    result = a - b

    assert result is not a
    assert result is not b


def test_mul():
    assert Vector3D(1, 2, 3) * 3 == Vector3D(3, 6, 9)


def test_mul_non_scalar():
    with pytest.raises(TypeError):
        Vector3D(1, 2, 3) * "5"


def test_mul_new_instance():
    a = Vector3D(1, 2, 3)
    result = a * 3

    assert result is not a


def test_rmul():
    assert 3 * Vector3D(1, 2, 3) == Vector3D(3, 6, 9)


def test_rmul_non_scalar():
    with pytest.raises(TypeError):
        "5" * Vector3D(1, 2, 3)


def test_rmul_new_instance():
    a = Vector3D(1, 2, 3)
    result = 3 * a

    assert result is not a


def test_truediv():
    assert Vector3D(3, 6, 9) / 3 == Vector3D(1, 2, 3)


def test_truediv_non_scalar():
    with pytest.raises(TypeError):
        Vector3D(3, 6, 9) / "3"


def test_truediv_string():
    with pytest.raises(TypeError):
        "abc" / Vector3D(1, 2, 3)


def test_truediv_new_instance():
    a = Vector3D(3, 6, 9)
    result = a / 3

    assert result is not a


def test_truediv_zero():
    with pytest.raises(ZeroDivisionError):
        Vector3D(1, 1, 1) / 0


def test_neg():
    assert -Vector3D(1, 2, 3) == Vector3D(-1, -2, -3)


def test_neg_new_instance():
    a = Vector3D(3, 6, 9)
    result = -a

    assert result is not a


def test_arithmetics_do_not_mutate():
    a = Vector3D(5, 5, 5)
    b = Vector3D(2, 1, 1)

    a + b
    a - b
    a * 2
    a / 2
    -a

    assert a == Vector3D(5, 5, 5)
    assert b == Vector3D(2, 1, 1)


def test_copy_distinct_but_equal():
    a = Vector3D(1, 2, 3)
    b = a.copy()

    assert b == a
    assert b is not a


def test_copy_is_independent():
    a = Vector3D(1, 2, 3)
    b = a.copy()

    b.x = 9

    assert a.x == 1


def test_dot_orthogonal():
    assert Vector3D(1, 0, 0).dot(Vector3D(0, 1, 0)) == 0.0


def test_dot_parallel():
    assert Vector3D(2, 0, 0).dot(Vector3D(3, 0, 0)) == 6.0


def test_dot_general():
    assert Vector3D(1, 2, 3).dot(Vector3D(4, 5, 6)) == 32.0


def test_magnitude():
    assert Vector3D(2, 3, 6).magnitude() == 7.0


def test_magnitude_zero_vector():
    assert Vector3D(0, 0, 0).magnitude() == 0.0


def test_normalize_produces_unit_length():
    v = Vector3D(2, 3, 6)
    v.normalize()

    assert math.isclose(v.magnitude(), 1.0)


def test_normalize_returns_self():
    v = Vector3D(2, 3, 6)
    result = v.normalize()

    assert result is v


def test_normalize_zero_vector():
    with pytest.raises(ZeroDivisionError):
        Vector3D(0, 0, 0).normalize()