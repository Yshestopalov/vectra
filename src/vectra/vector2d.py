"""
This module includes Vector2D involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

Part of the vectra library. Vector2D is mutable, new vector is created in operations involving two or more vectors.
"""

from __future__ import annotations

import math

from .utils import lerp

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
