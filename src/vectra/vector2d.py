"""
This module includes Vector2D involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

Part of the vectra library. Vector2D is mutable, new vector is created in operations involving two or more vectors.
"""

from __future__ import annotations

import math
import random

from .utils import lerp, clamp, approx_equal

class Vector2D:
    """
    A 2D vector involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

    Vector2D is mutable, when you need to make a copy use .copy() to safely create a duplicate.
    Vector2D uses a screen-space coordinate convention: Y axis increases downwards.

    Attributes:
        x (float): Vector's horizontal component.
        y (float): Vector's vertical component.
    """

    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a vector from its components.

        Args:
            x: Horizontal component.
            y: Vertical component.
        """
        self.x = x
        self.y = y

    def __add__(self, other: Vector2D) -> Vector2D:
        """
        Add two vectors together.

        Args:
            other: Vector to add.

        Returns:
            The sum of the two vectors.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
    
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        """
        Subtract one vector from another.

        Args:
            other: Vector to subtract.

        Returns:
            The difference of the two vectors.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
        
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector2D:
        """
        Scale the vector by a scalar (e.g. 2, 0.5, -1).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> Vector2D:
        """
        Scale the vector by a scalar (right multiplication).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.
        """
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> Vector2D:
        """
        Scale the vector by the reciprocal of a scalar (e.g. 1/2, 1/3, 3/5).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.

        Raises:
            ZeroDivisionError: If scalar is 0.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        
        return Vector2D(self.x / scalar, self.y / scalar)

    def __neg__(self) -> Vector2D:
        """
        Negate the vector.

        Returns:
            The negated vector.
        """
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        """
        Check if the vector is equal to an object.

        Args:
            other: Object to compare.

        Returns:
            True if the vector is equal to the object, False otherwise.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
        
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        """
        Get the string representation of the vector.

        Returns:
            The string representation of the vector.
        """
        return f"Vector2D({self.x}, {self.y})"

    def copy(self) -> Vector2D:
        """
        Create a copy of the vector.

        Returns:
            A new instance of Vector2D with the same components.
        """
        return Vector2D(self.x, self.y)

    def dot(self, other: Vector2D) -> float:
        """
        Calculate the dot product of two vectors.

        Args:
            other: The vector to dot with.

        Returns:
            The scalar dot product.

        >>> Vector2D(1.0, 0.0).dot(Vector2D(0.0, 1.0))
        0.0
        """
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        """
        Calculate the length of the vector.

        Returns:
            The magnitude of the vector.

        >>> Vector2D(3, 4).magnitude()
        5.0
        """
        return math.hypot(self.x, self.y)

    def normalize(self) -> Vector2D:
        """
        Calculate the unit vector of a vector.

        Returns:
            self, the normalized version.

        Raises:
            ZeroDivisionError: If this vector's magnitude is 0.

        >>> Vector2D(3, 4).normalize()
        Vector2D(0.6, 0.8)
        """
        mag = self.magnitude()
    
        self.x /= mag
        self.y /= mag

        return self

    def distance_to(self, other: Vector2D) -> float:
        """
        Calculate the Euclidean (straight-line) distance to another vector.

        Args:
            other: The vector to measure distance to.

        Returns:
            The distance between this vector and other.

        >>> Vector2D(0, 0).distance_to(Vector2D(3, 4))
        5.0
        """
        return math.sqrt(self.distance_squared_to(other))

    def distance_squared_to(self, other: Vector2D) -> float:
        """
        Calculate the squared Euclidean distance to another vector.

        Args:
            other: The vector to measure the squared distance to.

        Returns:
            The squared distance between this vector and other.

        >>> Vector2D(0, 0).distance_squared_to(Vector2D(3, 4))
        25
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def manhattan_distance_to(self, other: Vector2D) -> float:
        """
        Calculate the Manhattan (grid-based) distance to another vector.

        Args:
            other: The vector to measure the Manhattan distance to.

        Returns:
            The Manhattan distance between this vector and other.

        >>> Vector2D(0, 0).manhattan_distance_to(Vector2D(3, 4))
        7
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle(self) -> float:
        """
        Calculate this vector's angle from the positive x-axis.

        Returns:
            The angle in radians, in (-pi, pi].

        >>> Vector2D(1, 0).angle()
        0.0
        """
        return math.atan2(self.y, self.x)

    def angle_to(self, other: Vector2D) -> float:
        """
        Calculate the unsigned angle between this vector and another.

        Args:
            other: The vector to measure the angle to.

        Returns:
            The angle in radians, in [0, pi].

        Raises:
            ZeroDivisionError: If either vector has a magnitude of 0.

        >>> Vector2D(1, 0).angle_to(Vector2D(0, 1))
        1.5707963267948966
        """
        cos_theta = self.dot(other) / (self.magnitude() * other.magnitude())
        cos_theta = max(-1, min(1, cos_theta))

        return math.acos(cos_theta)

    def direction_to(self, other: Vector2D) -> Vector2D:
        """
        Calculate the normalized direction from this vector to another.

        Args:
            other: The vector to point towards.

        Returns:
            A new unit vector pointing from self towards other.

        Raises:
            ZeroDivisionError: If self and other are the same vector.

        >>> Vector2D(0, 0).direction_to(Vector2D(0, 5))
        Vector2D(0.0, 1.0)
        """
        return (other - self).normalize()

    def rotated(self, radians: float) -> Vector2D:
        """
        Calculate a new vector rotated by an angle.

        Args:
            radians: Angle to rotate by, in radians.

        Returns:
            A new vector, rotated from this one.

        >>> result = Vector2D(1, 0).rotated(math.pi / 2)
        >>> round(result.x, 10), round(result.y, 10)
        (0.0, 1.0)
        """
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        return Vector2D(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )

    def rotate(self, radians: float) -> Vector2D:
        """
        Rotate this vector by an angle.

        Args:
            radians: Angle to rotate by, in radians.

        Returns:
            self, after rotating in place.

        >>> v = Vector2D(1, 0)
        >>> _ = v.rotate(math.pi / 2)
        >>> round(v.x, 10), round(v.y, 10)
        (0.0, 1.0)
        """
        rotated = self.rotated(radians)

        self.x = rotated.x
        self.y = rotated.y

        return self
    
    def perpendicular(self) -> Vector2D:
        """
        Calculate a new vector rotated 90 degrees counter clockwise.

        Returns:
            A new vector, perpendicular to this one.

        >>> Vector2D(1, 0).perpendicular()
        Vector2D(0, 1)
        """
        return Vector2D(-self.y, self.x)

    def perpendicular_cw(self) -> Vector2D:
        """
        Calculate a new vector rotated 90 degrees clockwise.

        Returns:
            A new vector, perpendicular to this one.

        >>> Vector2D(1, 0).perpendicular_cw()
        Vector2D(0, -1)
        """
        return Vector2D(self.y, -self.x)

    def lerp(self, other: Vector2D, t: float) -> Vector2D:
        """
        Linearly interpolate from this vector toward another.
        
        Args:
            other: The vector to interpolate toward.
            t: Interpolation factor, in [0, 1].

        Returns:
            A new vector, interpolated between self and other.

        >>> Vector2D(0, 0).lerp(Vector2D(10, 10), 0.5)
        Vector2D(5.0, 5.0)
        """
        return Vector2D(lerp(self.x, other.x, t), lerp(self.y, other.y, t))

    def move_toward(self, target: Vector2D, max_distance: float) -> Vector2D:
        """
        Calculate a new vector stepped toward a target.

        Args: 
            target: The vector to move toward.
            max_distance: The maximum distance to move by this call.

        Returns:
            A new vector, stepped toward target. If self and target are the same point, returns a copy of self.

        >>> Vector2D(0, 0).move_toward(Vector2D(10, 0), 4)
        Vector2D(4.0, 0.0)
        >>> Vector2D(0, 0).move_toward(Vector2D(2, 0), 10)
        Vector2D(2, 0)
        >>> Vector2D(3, 4).move_toward(Vector2D(3, 4), 5)
        Vector2D(3, 4)
        """
        remaining = self.distance_to(target)

        if remaining == 0:
            return self.copy()

        if remaining <= max_distance:
            return target.copy()

        return self + self.direction_to(target) * max_distance

    def project_onto(self, other: Vector2D) -> Vector2D:
        """
        Calculate the projection of this vector onto another.

        Args:
            other: The vector to project onto.

        Returns:
            A new vector, the projection of self onto other.

        Raises:
            ZeroDivisionError: If other has a magnitude of 0.

        >>> Vector2D(2, 2).project_onto(Vector2D(1, 0))
        Vector2D(2.0, 0.0)
        """
        return other * (self.dot(other) / other.dot(other))

    def reject_from(self, other: Vector2D) -> Vector2D:
        """
        Calculate the rejection of this vector from another.

        Args:
            other: The vector to reject from.

        Returns:
            A new vector, the rejection of self from other.

        Raises:
            ZeroDivisionError: If other has a magnitude of 0.

        >>> Vector2D(2, 2).reject_from(Vector2D(1, 0))
        Vector2D(0.0, 2.0)
        """
        return self - self.project_onto(other)

    def reflect(self, normal: Vector2D) -> Vector2D:
        """
        Calculate this vector reflected off a surface.

        Args:
            normal: The unit normal of the surface to reflect off, must be normalized.

        Returns:
            A new vector, reflected across normal.

        >>> Vector2D(1, -1).reflect(Vector2D(0, 1))
        Vector2D(1, 1)
        """
        return self - normal * (2 * self.dot(normal))

    def cross(self, other: Vector2D) -> float:
        """
        Calculate the 2D scalar cross product with another vector.

        Args:
            other: The vector to cross with.

        Returns:
            The scalar cross product.

        >>> Vector2D(1, 0).cross(Vector2D(0, 1))
        1
        """
        return self.x * other.y - self.y * other.x
    
    def abs(self) -> Vector2D:
        """
        Calculate a new vector with each component's absolute value.

        Returns:
            A new vector, with non-negative components.

        >>> Vector2D(-1, -2).abs()
        Vector2D(1, 2)
        """
        return Vector2D(abs(self.x), abs(self.y))

    def sign(self) -> Vector2D:
        """
        Calculate a new vector indicating each component's sign.

        Returns: 
            A new vector of -1/0/1 components.

        >>> Vector2D(-5, 3).sign()
        Vector2D(-1, 1)
        """
        def _sign(value: float) -> int:
            return (value > 0) - (value < 0)

        return Vector2D(_sign(self.x), _sign(self.y))

    def round(self, digits: int = 0) -> Vector2D:
        """
        Calculate a new vector with each component rounded.

        Args: 
            digits: Number of decimal place to round to.

        Returns:
            A new vector, with rounded components.

        >>> Vector2D(1.234, 5.678).round(1)
        Vector2D(1.2, 5.7)
        """
        return Vector2D(round(self.x, digits), round(self.y, digits))

    def floor(self) -> Vector2D:
        """
        Calculate a new vector with each component floored.

        Returns:
            A new vector, with floored components.

        >>> Vector2D(1.7, -1.2).floor()
        Vector2D(1, -2)
        """
        return Vector2D(math.floor(self.x), math.floor(self.y))

    def ceil(self) -> Vector2D:
        """
        Calculate a new vector with each component ceiled.
        
        Returns:
            A new vector, with ceiled components.

        >>> Vector2D(1.2, -1.7).ceil()
        Vector2D(2, -1)
        """
        return Vector2D(math.ceil(self.x), math.ceil(self.y))

    def clamp_magnitude(self, max_length: float) -> Vector2D:
        """
        Calculate a new vector capped to a maximum length.

        Args:
            max_length: The maximum allowed magnitude.

        Returns:
            A new vector, with magnitude at most max_length.

        >>> Vector2D(3, 4).clamp_magnitude(2.5)
        Vector2D(1.5, 2.0)
        """
        mag = self.magnitude()

        if mag <= max_length:
            return self.copy()

        return self * (max_length / mag)

    def clamp(self, minimum: Vector2D, maximum: Vector2D) -> Vector2D:
        """
        Calculate a new vector with each component clamped between bounds.

        Args:
            minimum: Vector's lower bound for each component.
            maximum: Vector's upper bound for each component.

        Returns:
            A new vector, component-wise clamped.

        >>> Vector2D(15, -5).clamp(Vector2D(0, 0), Vector2D(10, 10))
        Vector2D(10, 0)
        """
        return Vector2D(
            clamp(self.x, minimum.x, maximum.x),
            clamp(self.y, minimum.y, maximum.y),
        )

    def is_zero(self, epsilon: float = 1e-9) -> bool:
        """
        Check whether this vector's magnitude is approximately 0.

        Args:
            epsilon: Maximum magnitude still considered 0.

        Returns:
            True if the magnitude is below epsilon.

        >>> Vector2D(0, 0).is_zero()
        True
        """
        return self.magnitude() < epsilon

    def is_normalized(self, epsilon: float = 1e-9) -> bool:
        """
        Check whether this vector's magnitude is approximately 1.

        Args:
            epsilon: Maximum allowed deviation from 1.

        Returns:
            True if the magnitude is within epsilon of 1.

        >>> Vector2D(1, 0).is_normalized()
        True
        """
        return abs(self.magnitude() - 1) < epsilon

    def is_approx_equal(self, other: Vector2D, epsilon: float = 1e-9) -> bool:
        """
        Check whether this vector's components are approximately equal to another.

        Args:
            other: The vector to compare against.
            epsilon: Maximum allowed difference per component.

        Returns:
            True if both components are within epsilon of other's.

        >>> Vector2D(0.1 + 0.2, 1).is_approx_equal(Vector2D(0.3, 1))
        True
        """
        return approx_equal(self.x, other.x, epsilon) and approx_equal(self.y, other.y, epsilon)

    def to_tuple(self) -> tuple[float, float]:
        """
        Convert this vector to a tuple.

        Returns:
            A tuple of (x, y).

        >>> Vector2D(3, 4).to_tuple()
        (3, 4)
        """
        return (self.x, self.y)

    def to_int_tuple(self) -> tuple[int, int]:
        """
        Convert this vector to an integer tuple.

        Returns:
            A tuple of (int(x), int(y)).

        >>> Vector2D(3.9, 4.1).to_int_tuple()
        (3, 4)
        """
        return (int(self.x), int(self.y))

    def to_list(self) -> list[float]:
        """
        Convert this vector to a list.

        Returns:
            A list of [x, y].

        >>> Vector2D(3, 4).to_list()
        [3, 4]
        """
        return [self.x, self.y]

    def to_complex(self) -> complex:
        """
        Convert this vector to a complex number.

        Returns:
            A complex number, x + yj.

        >>> Vector2D(3, 4).to_complex()
        (3+4j)
        """
        return complex(self.x, self.y)

    @staticmethod
    def min(a: Vector2D, b: Vector2D) -> Vector2D:
        """
        Calculate the component-wise minimum of two vectors.

        Args:
            a: The first vector.
            b: The second vector.

        Returns:
            A new vector, the component-wise minimum of a and b.

        >>> Vector2D.min(Vector2D(1, 5), Vector2D(3, 2))
        Vector2D(1, 2)
        """
        return Vector2D(min(a.x, b.x), min(a.y, b.y))

    @staticmethod
    def max(a: Vector2D, b: Vector2D) -> Vector2D:
        """
        Calculate the component-wise maximum of two vectors.

        Args:
            a: The first vector.
            b: The second vector.

        Returns:
            A new vector, the component-wise maximum of a and b.

        >>> Vector2D.max(Vector2D(1, 5), Vector2D(3, 2))
        Vector2D(3, 5)
        """
        return Vector2D(max(a.x, b.x), max(a.y, b.y))

    @classmethod
    def from_angle(cls, radians: float, length: float = 1) -> Vector2D:
        """
        Construct a vector pointing at a given angle.

        Args: 
            radians: Angle from the positive x-axis, in radians.
            length: Magnitude of the resulting vector.

        Returns:
            A new vector, at the given angle and length.

        >>> result = Vector2D.from_angle(math.pi / 2)
        >>> round(result.x, 10), round(result.y, 10)
        (0.0, 1.0)
        """
        return cls(length * math.cos(radians), length * math.sin(radians))

    @classmethod
    def from_tuple(cls, values: tuple[float, float]) -> Vector2D:
        """
        Construct a vector from a tuple.

        Args:
            values: A two-element tuple.

        Returns:
            A new vector, with the tuple's components.

        >>> Vector2D.from_tuple((3, 4))
        Vector2D(3, 4)
        """
        x, y = values
        return cls(x, y)

    @classmethod
    def random_unit(cls) -> Vector2D:
        """
        Construct a random unit-length vector, pointing in any direction.

        Returns:
            A new vector with magnitude 1 and a random angle.
        """
        return cls.from_angle(random.uniform(0, 2 * math.pi)) 

    @classmethod
    def zero(cls) -> Vector2D:
        """
        Construct the zero vector.

        Returns:
            A new vector at (0, 0).

        >>> Vector2D.zero()
        Vector2D(0, 0)
        """
        return cls(0, 0)
        
    @classmethod
    def one(cls) -> Vector2D:
        """
        Construct the one vector.

        Returns:
            A new vector at (1, 1).

        >>> Vector2D.one()
        Vector2D(1, 1)
        """
        return cls(1, 1)

    @classmethod
    def up(cls) -> Vector2D:
        """
        Construct the up vector.

        Returns:
            A new vector at (0, -1).

        >>> Vector2D.up()
        Vector2D(0, -1)
        """
        return cls(0, -1)

    @classmethod
    def down(cls) -> Vector2D:
        """
        Construct the down vector.

        Returns:
            A new vector at (0, 1).

        >>> Vector2D.down()
        Vector2D(0, 1)
        """
        return cls(0, 1)

    @classmethod
    def left(cls) -> Vector2D:
        """
        Construct the left vector.

        Returns:
            A new vector at (-1, 0).

        >>> Vector2D.left()
        Vector2D(-1, 0)
        """
        return cls(-1, 0)

    @classmethod
    def right(cls) -> Vector2D:
        """
        Construct the right vector.

        Returns:
            A new vector at (1, 0).

        >>> Vector2D.right()
        Vector2D(1, 0)
        """
        return cls(1, 0)
