"""
This module includes Vector2D involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

Part of the vectra library. Vector2D is mutable, new vector is created in operations involving two or more vectors.
"""

from __future__ import annotations

import math

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
        25.0
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
            The angle in radians.

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
            The angle in radians.

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
