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


def test_arithmetics_do_not_mutate():
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


def test_angle_along_positive_x_axis():
    assert Vector2D(1, 0).angle() == 0.0


def test_angle_to_perpendicular_vector():
    assert math.isclose(Vector2D(1, 0).angle_to(Vector2D(0, 1)), math.pi / 2)


def test_angle_to_parallel_vector():
    assert math.isclose(Vector2D(2, 0).angle_to(Vector2D(5, 0)), 0.0)


def test_angle_to_zero():
    with pytest.raises(ZeroDivisionError):
        Vector2D(1, 0).angle_to(Vector2D(0, 0))


def test_angle_to_symmetric():
    a = Vector2D(1, 0)
    b = Vector2D(0, 1)
    assert math.isclose(a.angle_to(b), b.angle_to(a))


def test_direction_to():
    assert Vector2D(0, 0).direction_to(Vector2D(5, 0)) == Vector2D(1.0, 0.0)


def test_direction_to_zero():
    with pytest.raises(ZeroDivisionError):
        Vector2D(0, 0).direction_to(Vector2D(0, 0))


def test_rotated_quarter_turn():
    result = Vector2D(1, 0).rotated(math.pi / 2)
    assert math.isclose(result.x, 0, abs_tol=1e-9)
    assert math.isclose(result.y, 1, abs_tol=1e-9)


def test_rotated_full_turn():
    v = Vector2D(3, 4)
    result = v.rotated(2 * math.pi)
    assert math.isclose(result.x, v.x, abs_tol=1e-9)
    assert math.isclose(result.y, v.y, abs_tol=1e-9)


def test_rotated_preserves_magnitude():
    v = Vector2D(3, 4)
    result = v.rotated(1.234)
    assert math.isclose(result.magnitude(), v.magnitude())


def test_rotated_returns_new_instance():
    v = Vector2D(1, 0)
    result = v.rotated(math.pi / 2)
    assert result is not v


def test_rotated_does_not_mutate():
    v = Vector2D(1, 0)
    v.rotated(math.pi / 2)
    assert v == Vector2D(1, 0)


def test_rotate_mutates_in_place():
    v = Vector2D(1, 0)
    result = v.rotate(math.pi / 2)
    assert result is v
    assert math.isclose(v.x, 0, abs_tol=1e-9)
    assert math.isclose(v.y, 1, abs_tol=1e-9)


def test_perpendicular():
    assert Vector2D(1, 0).perpendicular() == Vector2D(0, 1)


def test_perpendicular_preserves_magnitude():
    v = Vector2D(3, 4)
    assert math.isclose(v.perpendicular().magnitude(), v.magnitude())


def test_perpendicular_returns_new_instance():
    v = Vector2D(1, 0)
    assert v.perpendicular() is not v


def test_perpendicular_cw():
    assert Vector2D(1, 0).perpendicular_cw() == Vector2D(0, -1)


def test_perpendicular_and_perpendicular_cw_are_opposite():
    v = Vector2D(3, 4)
    assert v.perpendicular() == -v.perpendicular_cw()


def test_lerp_midpoint():
    assert Vector2D(0, 0).lerp(Vector2D(10, 10), 0.5) == Vector2D(5.0, 5.0)


def test_lerp_endpoints():
    assert Vector2D(0, 0).lerp(Vector2D(10, 10), 0) == Vector2D(0, 0)
    assert Vector2D(0, 0).lerp(Vector2D(10, 10), 1) == Vector2D(10, 10)


def test_lerp_returns_new_instance():
    a = Vector2D(0, 0)
    b = Vector2D(10, 10)
    result = a.lerp(b, 0.5)
    assert result is not a
    assert result is not b


def test_lerp_does_not_mutate():
    a = Vector2D(0, 0)
    b = Vector2D(10, 10)
    a.lerp(b, 0.5)
    assert a == Vector2D(0, 0)
    assert b == Vector2D(10, 10)


def test_lerp_extrapolates_beyond():
    assert Vector2D(0, 0).lerp(Vector2D(10, 10), 2) == Vector2D(20, 20)


def test_move_toward_partial_step():
    result = Vector2D(0, 0).move_toward(Vector2D(10, 0), 4)
    assert result == Vector2D(4.0, 0.0)


def test_move_toward_does_not_overshoot():
    result = Vector2D(0, 0).move_toward(Vector2D(2, 0), 10)
    assert result == Vector2D(2.0, 0.0)


def test_move_toward_already_at_target():
    result = Vector2D(3, 4).move_toward(Vector2D(3, 4), 5)
    assert result == Vector2D(3, 4)


def test_move_toward_returns_new_instance():
    a = Vector2D(0, 0)
    target = Vector2D(10, 0)
    result = a.move_toward(target, 4)
    assert result is not a


def test_move_toward_does_not_mutate_self():
    a = Vector2D(0, 0)
    a.move_toward(Vector2D(10, 0), 4)
    assert a == Vector2D(0, 0)


def test_move_toward_preserves_distance_relationship():
    a = Vector2D(0, 0)
    target = Vector2D(10, 0)
    result = a.move_toward(target, 4)
    assert result.distance_to(target) < a.distance_to(target)


def test_move_toward_zero_max_distance():
    result = Vector2D(0, 0).move_toward(Vector2D(10, 0), 0)
    assert result == Vector2D(0, 0)


def test_project_onto():
    assert Vector2D(2, 2).project_onto(Vector2D(1, 0)) == Vector2D(2.0, 0.0)


def test_project_onto_perpendicular():
    result = Vector2D(0, 5).project_onto(Vector2D(1, 0))
    assert result == Vector2D(0.0, 0.0)


def test_project_onto_parallel():
    result = Vector2D(3, 0).project_onto(Vector2D(1, 0))
    assert result == Vector2D(3.0, 0.0)


def test_project_onto_zero():
    with pytest.raises(ZeroDivisionError):
        Vector2D(1, 1).project_onto(Vector2D(0, 0))


def test_project_onto_returns_new_instance():
    a = Vector2D(2, 2)
    other = Vector2D(1, 0)
    result = a.project_onto(other)
    assert result is not a


def test_project_onto_does_not_mutate():
    a = Vector2D(2, 2)
    other = Vector2D(1, 0)
    a.project_onto(other)
    assert a == Vector2D(2, 2)
    assert other == Vector2D(1, 0)


def test_reject_from():
    assert Vector2D(2, 2).reject_from(Vector2D(1, 0)) == Vector2D(0.0, 2.0)


def test_reject_from_parallel():
    result = Vector2D(3, 0).reject_from(Vector2D(1, 0))
    assert result == Vector2D(0.0, 0.0)


def test_reject_from_zero():
    with pytest.raises(ZeroDivisionError):
        Vector2D(1, 1).reject_from(Vector2D(0, 0))


def test_project_and_reject_combine_to_self():
    a = Vector2D(3, 4)
    other = Vector2D(1, 0)
    result = a.project_onto(other) + a.reject_from(other)
    assert result == a


def test_reject_from_returns_new_instance():
    a = Vector2D(2, 2)
    other = Vector2D(1, 0)
    result = a.reject_from(other)
    assert result is not a


def test_reflect_off_horizontal_surface():
    assert Vector2D(1, -1).reflect(Vector2D(0, 1)) == Vector2D(1.0, 1.0)


def test_reflect_straight_hit_reverses():
    result = Vector2D(0, -5).reflect(Vector2D(0, 1))
    assert result == Vector2D(0.0, 5.0)


def test_reflect_parallel_to_surface_unchanged():
    result = Vector2D(1, 0).reflect(Vector2D(0, 1))
    assert result == Vector2D(1.0, 0.0)


def test_reflect_preserves_magnitude():
    v = Vector2D(3, -4)
    normal = Vector2D(0, 1)
    assert math.isclose(v.reflect(normal).magnitude(), v.magnitude())


def test_reflect_returns_new_instance():
    v = Vector2D(1, -1)
    normal = Vector2D(0, 1)
    result = v.reflect(normal)
    assert result is not v


def test_reflect_does_not_mutate():
    v = Vector2D(1, -1)
    normal = Vector2D(0, 1)
    v.reflect(normal)
    assert v == Vector2D(1, -1)


def test_cross_perpendicular():
    assert Vector2D(1, 0).cross(Vector2D(0, 1)) == 1


def test_cross_parallel_is_zero():
    assert Vector2D(2, 0).cross(Vector2D(5, 0)) == 0


def test_cross_anti_commutative():
    a = Vector2D(1, 0)
    b = Vector2D(0, 1)
    assert a.cross(b) == -b.cross(a)


def test_cross_sign_indicates_direction():
    a = Vector2D(1, 0)
    counter_clockwise = Vector2D(0, 1)
    clockwise = Vector2D(0, -1)
    assert a.cross(counter_clockwise) > 0
    assert a.cross(clockwise) < 0


def test_clamp_magnitude_scales_down():
    assert Vector2D(3, 4).clamp_magnitude(2.5) == Vector2D(1.5, 2.0)


def test_clamp_magnitude_short_vector_unchanged():
    assert Vector2D(1, 1).clamp_magnitude(10) == Vector2D(1, 1)


def test_clamp_magnitude_returns_new_instance():
    v = Vector2D(3, 4)
    result = v.clamp_magnitude(2.5)
    assert result is not v


def test_clamp_magnitude_does_not_mutate():
    v = Vector2D(3, 4)
    v.clamp_magnitude(2.5)
    assert v == Vector2D(3, 4)


def test_clamp_within_bounds():
    result = Vector2D(5, 5).clamp(Vector2D(0, 0), Vector2D(10, 10))
    assert result == Vector2D(5, 5)


def test_clamp_above_bounds():
    result = Vector2D(15, -5).clamp(Vector2D(0, 0), Vector2D(10, 10))
    assert result == Vector2D(10, 0)


def test_clamp_returns_new_instance():
    v = Vector2D(15, -5)
    result = v.clamp(Vector2D(0, 0), Vector2D(10, 10))
    assert result is not v


def test_abs():
    assert Vector2D(-3, 4).abs() == Vector2D(3, 4)


def test_abs_returns_new_instance():
    v = Vector2D(-3, 4)
    assert v.abs() is not v


def test_sign_positive_and_negative():
    assert Vector2D(-5, 3).sign() == Vector2D(-1, 1)


def test_sign_zero_component():
    assert Vector2D(0, -2).sign() == Vector2D(0, -1)


def test_round():
    assert Vector2D(1.234, 5.678).round(1) == Vector2D(1.2, 5.7)


def test_round_default_digits():
    assert Vector2D(1.4, 1.6).round() == Vector2D(1, 2)


def test_floor():
    assert Vector2D(1.7, -1.2).floor() == Vector2D(1, -2)


def test_ceil():
    assert Vector2D(1.2, -1.7).ceil() == Vector2D(2, -1)


def test_is_zero_true():
    assert Vector2D(0, 0).is_zero()


def test_is_zero_false():
    assert not Vector2D(0.1, 0).is_zero()


def test_is_normalized_true():
    assert Vector2D(1, 0).is_normalized()


def test_is_normalized_false():
    assert not Vector2D(2, 0).is_normalized()


def test_is_approx_equal_true():
    assert Vector2D(0.1 + 0.2, 1).is_approx_equal(Vector2D(0.3, 1))


def test_is_approx_equal_false():
    assert not Vector2D(1, 1).is_approx_equal(Vector2D(1.1, 1))


def test_to_tuple():
    assert Vector2D(3, 4).to_tuple() == (3, 4)


def test_to_int_tuple():
    assert Vector2D(3.9, 4.1).to_int_tuple() == (3, 4)


def test_to_list():
    assert Vector2D(3, 4).to_list() == [3, 4]


def test_to_complex():
    assert Vector2D(3, 4).to_complex() == complex(3, 4)


def test_from_angle():
    result = Vector2D.from_angle(math.pi / 2)
    assert math.isclose(result.x, 0, abs_tol=1e-9)
    assert math.isclose(result.y, 1, abs_tol=1e-9)


def test_from_angle_with_length():
    assert Vector2D.from_angle(0, length=5) == Vector2D(5.0, 0.0)


def test_from_tuple():
    assert Vector2D.from_tuple((3, 4)) == Vector2D(3, 4)


def test_random_unit_has_magnitude_one():
    assert math.isclose(Vector2D.random_unit().magnitude(), 1.0)


def test_min():
    assert Vector2D.min(Vector2D(1, 5), Vector2D(3, 2)) == Vector2D(1, 2)


def test_max():
    assert Vector2D.max(Vector2D(1, 5), Vector2D(3, 2)) == Vector2D(3, 5)


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


def test_constructors_return_new_instances():
    assert Vector2D.zero() is not Vector2D.zero()
    assert Vector2D.one() is not Vector2D.one()
    assert Vector2D.up() is not Vector2D.up()
    assert Vector2D.down() is not Vector2D.down()
    assert Vector2D.left() is not Vector2D.left()
    assert Vector2D.right() is not Vector2D.right()