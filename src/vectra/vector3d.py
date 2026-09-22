"""
This module includes Vector3D involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

Part of the vectra library. Vector3D is mutable, new vector is created in operations involving two or more vectors.
"""

from __future__ import annotations


class Vector3D:
    """
    A 3D vector involving arithmetic (e.g. addition, subtraction) and geometric operations (e.g. distance, dot product).

    Vector3D is mutable, when you need to make a copy use .copy() to safely create a duplicate.

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

        >>> Vector3D(2, 3, 6).normalize()
        Vector3D(0.2857142857142857, 0.42857142857142855, 0.8571428571428571)
        """
        mag = self.magnitude()

        self.x /= mag
        self.y /= mag
        self.z /= mag

        return self