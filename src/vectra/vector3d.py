"""
This module includes Vector3D involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

Part of the vectra library. Vector3D is mutable, new vector is created in operations involving two or more vectors.
"""

from __future__ import annotations

import math


class Vector3D:
    """
    A 3D vector involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

    Vector3D is mutable, when you need to make a copy use .copy() to safely create a duplicate.
    Vector3D uses a left-handed coordinate system.

    Attributes:
        x (float): Vector's horizontal component.
        y (float): Vector's vertical component.
        z (float): Vector's depth component.
    """

    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initialize a vector from its components.

        Args:
            x: Horizontal component.
            y: Vertical component.
            z: Depth component.
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vector3D) -> Vector3D:
        """
        Add two vectors together.

        Args:
            other: Vector to add.

        Returns:
            The sum of the two vectors.
        """
        if not isinstance(other, Vector3D):
            return NotImplemented

        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3D) -> Vector3D:
        """
        Subtract one vector from another.

        Args:
            other: Vector to subtract.

        Returns:
            The difference of the two vectors.
        """
        if not isinstance(other, Vector3D):
            return NotImplemented

        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> Vector3D:
        """
        Scale the vector by a scalar (e.g. 2, 0.5, -1).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> Vector3D:
        """
        Scale the vector by a scalar (right multiplication).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.
        """
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> Vector3D:
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

        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self) -> Vector3D:
        """
        Negate the vector.

        Returns:
            The negated vector.
        """
        return Vector3D(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        """
        Check if the vector is equal to an object.

        Args:
            other: Object to compare.

        Returns:
            True if the vector is equal to the object, False otherwise.
        """
        if not isinstance(other, Vector3D):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self) -> str:
        """
        Get the string representation of the vector.

        Returns:
            The string representation of the vector.
        """
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def copy(self) -> Vector3D:
        """
        Create a copy of the vector.

        Returns:
            A new instance of Vector3D with the same components.
        """
        return Vector3D(self.x, self.y, self.z)

    def dot(self, other: Vector3D) -> float:
        """
        Calculate the dot product of two vectors.

        Args:
            other: The vector to dot with.

        Returns:
            The scalar dot product.

        >>> Vector3D(1.0, 0.0, 0.0).dot(Vector3D(0.0, 1.0, 0.0))
        0.0
        """
        if not isinstance(other, Vector3D):
            raise TypeError(f"expected Vector3D, got {type(other).__name__}")
        
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self) -> float:
        """
        Calculate the length of the vector.

        Returns:
            The magnitude of the vector.

        >>> Vector3D(2, 3, 6).magnitude()
        7.0
        """
        return math.hypot(self.x, self.y, self.z)

    def normalize(self) -> Vector3D:
        """
        Calculate the unit vector of a vector.

        Returns:
            self, the normalized version.

        Raises:
            ZeroDivisionError: If this vector's magnitude is 0.

        >>> Vector3D(0, 3, 4).normalize()
        Vector3D(0.0, 0.6, 0.8)
        """
        mag = self.magnitude()

        self.x /= mag
        self.y /= mag
        self.z /= mag

        return self

    def distance_to(self, other: Vector3D) -> float:
        """
        Calculate the Euclidean (straight-line) distance to another vector.

        Args:
            other: The vector to measure distance to.

        Returns:
            The distance between this vector and other.

        >>> Vector3D(0, 0, 0).distance_to(Vector3D(2, 3, 6))
        7.0
        """
        return math.sqrt(self.distance_squared_to(other))

    def distance_squared_to(self, other: Vector3D) -> float:
        """
        Calculate the squared Euclidean distance to another vector.

        Args:
            other: The vector to measure the squared distance to.

        Returns:
            The squared distance between this vector and other.

        >>> Vector3D(0, 0, 0).distance_squared_to(Vector3D(2, 3, 6))
        49
        """
        if not isinstance(other, Vector3D):
            raise TypeError(f"expected Vector3D, got {type(other).__name__}")
        
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def manhattan_distance_to(self, other: Vector3D) -> float:
        """
        Calculate the Manhattan (grid-based) distance to another vector.

        Args:
            other: The vector to measure the Manhattan distance to.

        Returns:
            The Manhattan distance between this vector and other.

        >>> Vector3D(0, 0, 0).manhattan_distance_to(Vector3D(2, 3, 6))
        11
        """
        if not isinstance(other, Vector3D):
            raise TypeError(f"expected Vector3D, got {type(other).__name__}")
        
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def angle_to(self, other: Vector3D) -> float:
        """
        Calculate the unsigned angle between this vector and another.

        Args:
            other: The vector to measure the angle to.

        Returns:
            The angle in radians, in [0, pi].

        Raises:
            ZeroDivisionError: If either vector has a magnitude of 0.

        >>> Vector3D(1, 0, 0).angle_to(Vector3D(0, 1, 0))
        1.5707963267948966
        """
        if not isinstance(other, Vector3D):
            raise TypeError(f"expected Vector3D, got {type(other).__name__}")
        
        cos_theta = self.dot(other) / (self.magnitude() * other.magnitude())
        cos_theta = max(-1, min(1, cos_theta))

        return math.acos(cos_theta)

    def direction_to(self, other: Vector3D) -> Vector3D:
        """
        Calculate the normalized direction from this vector to another.

        Args:
            other: The vector to point towards.

        Returns:
            A new unit vector pointing from self towards other.

        Raises:
            ZeroDivisionError: If self and other are the same vector.

        >>> Vector3D(0, 0, 0).direction_to(Vector3D(0, 0, 5))
        Vector3D(0.0, 0.0, 1.0)
        """
        return (other - self).normalize()

    @classmethod
    def one(cls) -> Vector3D:
        """
        Construct the one vector.

        Returns:
            A new vector at (1, 1, 1).

        >>> Vector3D.one()
        Vector3D(1, 1, 1)
        """
        return cls(1, 1, 1)

    @classmethod
    def zero(cls) -> Vector3D:
        """
        Construct the zero vector.

        Returns:
            A new vector at (0, 0, 0).

        >>> Vector3D.zero()
        Vector3D(0, 0, 0)
        """
        return cls(0, 0, 0)

    @classmethod
    def forward(cls) -> Vector3D:
        """
        Construct the forward vector.

        Returns:
            A new vector at (0, 0, 1).

        >>> Vector3D.forward()
        Vector3D(0, 0, 1)
        """
        return cls(0, 0, 1)

    @classmethod
    def backward(cls) -> Vector3D:
        """
        Construct the backward vector.

        Returns:
            A new vector at (0, 0, -1).

        >>> Vector3D.backward()
        Vector3D(0, 0, -1)
        """
        return cls(0, 0, -1)

    @classmethod
    def up(cls) -> Vector3D:
        """
        Construct the up vector.

        Returns:
            A new vector at (0, 1, 0).

        >>> Vector3D.up()
        Vector3D(0, 1, 0)
        """
        return cls(0, 1, 0)

    @classmethod
    def down(cls) -> Vector3D:
        """
        Construct the down vector.

        Returns:
            A new vector at (0, -1, 0).

        >>> Vector3D.down()
        Vector3D(0, -1, 0)
        """
        return cls(0, -1, 0)

    @classmethod
    def right(cls) -> Vector3D:
        """
        Construct the right vector.

        Returns:
            A new vector at (1, 0, 0).

        >>> Vector3D.right()
        Vector3D(1, 0, 0)
        """
        return cls(1, 0, 0)

    @classmethod
    def left(cls) -> Vector3D:
        """
        Construct the left vector.

        Returns:
            A new vector at (-1, 0, 0).

        >>> Vector3D.left()
        Vector3D(-1, 0, 0)
        """
        return cls(-1, 0, 0)    
