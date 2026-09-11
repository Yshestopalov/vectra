"""
2D vector implementation involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

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
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        """
        Subtract one vector from another.

        Args:
            other: Vector to subtract.

        Returns:
            The difference of the two vectors.
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector2D:
        """
        Scale the vector by a scalar (e.g. 2, 0.5, -1).

        Args:
            scalar: Value to scale the vector by.

        Returns:
            The scaled vector.
        """
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
        """
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

        >>> Vector2D(3, 4).normalize()
        Vector2D(0.6, 0.8)
        """
        mag = self.magnitude()
    
        self.x /= mag
        self.y /= mag

        return self

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
