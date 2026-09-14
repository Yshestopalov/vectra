"""
Tests for the Vector2D class.
"""

import math
import pytest

from vectra import Vector2D


def test_init():
    v = Vector2D(3, 4)
    assert v.x == 3
    assert v.y == 4


def test_repr():
    assert repr(Vector2D(1, 2)) == "Vector2D(1, 2)"


def test_eq_same():
    assert Vector2D(1, 2) == Vector2D(1, 2)


def test_eq_different():
    assert Vector2D(1, 2) != Vector2D(3, 4)


def test_eq_non_vector():
    assert Vector2D(1, 2) != 5
    assert Vector2D(1, 2) != "1, 2"


def test_unhashable():
    with pytest.raises(TypeError):
        hash(Vector2D(1, 2))


def test_add():
    assert Vector2D(1, 2) + Vector2D(3, 4) == Vector2D(4, 6)


def test_add_non_vector():
    with pytest.raises(TypeError):
        Vector2D(1, 2) + 5


def test_add_string():
    with pytest.raises(TypeError):
        "abc" + Vector2D(1, 2)


def test_add_new_instance():
    a = Vector2D(1, 2)
    b = Vector2D(3, 4)
    result = a + b

    assert result is not a
    assert result is not b


def test_sub():
    assert Vector2D(4, 6) - Vector2D(3, 4) == Vector2D(1, 2)


def test_sub_non_vector():
    with pytest.raises(TypeError):
        Vector2D(1, 2) - 5


def test_sub_string():
    with pytest.raises(TypeError):
        "abc" - Vector2D(1, 2)


def test_sub_new_instance():
    a = Vector2D(4, 6)
    b = Vector2D(3, 4)
    result = a - b

    assert result is not a
    assert result is not b


def test_mul():
    assert Vector2D(1, 2) * 3 == Vector2D(3, 6)


def test_mul_non_scalar():
    with pytest.raises(TypeError):
        Vector2D(1, 2) * "5"


def test_mul_new_instance():
    a = Vector2D(1, 2)
    result = a * 3

    assert result is not a


def test_rmul():
    assert 3 * Vector2D(1, 2) == Vector2D(3, 6)


def test_rmul_non_scalar():
    with pytest.raises(TypeError):
        "5" * Vector2D(1, 2)


def test_rmul_new_instance():
    a = Vector2D(1, 2)
    result = 3 * a

    assert result is not a


def test_truediv():
    assert Vector2D(3, 6) / 3 == Vector2D(1, 2)


def test_truediv_non_scalar():
    with pytest.raises(TypeError):
        Vector2D(3, 6) / "3"


def test_truediv_string():
    with pytest.raises(TypeError):
        "abc" / Vector2D(1, 2)


def test_truediv_new_instance():
    a = Vector2D(3, 6)
    result = a / 3

    assert result is not a


def test_truediv_zero():
    with pytest.raises(ZeroDivisionError):
        Vector2D(1, 1) / 0


def test_neg():
    assert -Vector2D(1, 2) == Vector2D(-1, -2)


def test_neg_new_instance():
    a = Vector2D(3, 6)
    result = -a

    assert result is not a


def test_arithmetics_do_not_mutate_operands():
    a = Vector2D(5, 5)
    b = Vector2D(2, 1)

    a + b
    a - b
    a * 2
    a / 2
    -a

    assert a == Vector2D(5, 5)
    assert b == Vector2D(2, 1)


def test_copy_distinct_but_equal():
    a = Vector2D(1, 2)
    b = a.copy()

    assert b == a
    assert b is not a


def test_copy_is_independent():
    a = Vector2D(1, 2)
    b = a.copy()

    b.x = 3

    assert a.x == 1


def test_dot_orthogonal():
    assert Vector2D(1, 0).dot(Vector2D(0, 1)) == 0.0


def test_dot_parallel():
    assert Vector2D(2, 0).dot(Vector2D(3, 0)) == 6.0


def test_magnitude():
    assert Vector2D(3, 4).magnitude() == 5.0


def test_magnitude_zero_vector():
    assert Vector2D(0, 0).magnitude() == 0.0


def test_normalize_produces_unit_length():
    v = Vector2D(3, 4)
    v.normalize()

    assert math.isclose(v.magnitude(), 1.0)


def test_normalize_returns_self():
    v = Vector2D(3, 4)
    result = v.normalize()

    assert result is v


def test_normalize_zero_vector():
    with pytest.raises(ZeroDivisionError):
        Vector2D(0, 0).normalize()


def test_zero():
    assert Vector2D.zero() == Vector2D(0, 0)


def test_one():
    assert Vector2D.one() == Vector2D(1, 1)


def test_up_and_down_are_opposite():
    assert Vector2D.up() == -Vector2D.down()


def test_left_and_right_are_opposite():
    assert Vector2D.left() == -Vector2D.right()


def test_up_matches_screen_space_convention():
    assert Vector2D.up().y < 0
    assert Vector2D.down().y > 0


def test_distance_to():
    assert Vector2D(0, 0).distance_to(Vector2D(3, 4)) == 5.0


def test_distance_to_same():
    assert Vector2D(1, 1).distance_to(Vector2D(1, 1)) == 0.0


def test_distance_to_non_vector():
    with pytest.raises(AttributeError):
        Vector2D(0, 0).distance_to(5)


def test_distance_to_symmetric():
    a = Vector2D(1, 2)
    b = Vector2D(4, 6)
    assert a.distance_to(b) == b.distance_to(a)


def test_distance_squared_to():
    assert Vector2D(0, 0).distance_squared_to(Vector2D(3, 4)) == 25.0


def test_distance_squared_to_same():
    assert Vector2D(1, 1).distance_squared_to(Vector2D(1, 1)) == 0.0


def test_distance_squared_to_non_vector():
    with pytest.raises(AttributeError):
        Vector2D(0, 0).distance_squared_to(5)


def test_distance_squared_to_symmetric():
    a = Vector2D(1, 2)
    b = Vector2D(4, 6)
    assert a.distance_squared_to(b) == b.distance_squared_to(a)


def test_manhattan_distance_to():
    assert Vector2D(0, 0).manhattan_distance_to(Vector2D(3, 4)) == 7


def test_manhattan_distance_to_same():
    assert Vector2D(1, 1).manhattan_distance_to(Vector2D(1, 1)) == 0.0


def test_manhattan_distance_to_non_vector():
    with pytest.raises(AttributeError):
        Vector2D(0, 0).manhattan_distance_to(5)


def test_manhattan_distance_to_symmetric():
    a = Vector2D(1, 2)
    b = Vector2D(4, 6)
    assert a.manhattan_distance_to(b) == b.manhattan_distance_to(a)


def test_constructors_return_new_instances():
    assert Vector2D.zero() is not Vector2D.zero()
    assert Vector2D.one() is not Vector2D.one()
    assert Vector2D.up() is not Vector2D.up()
    assert Vector2D.down() is not Vector2D.down()
    assert Vector2D.left() is not Vector2D.left()
    assert Vector2D.right() is not Vector2D.right()