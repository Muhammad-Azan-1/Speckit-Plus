"""
API Contracts for the Simple Calculator Library.

This module defines the function signatures for all arithmetic operations
provided by the calculator library, including type hints and docstrings.
"""

from numbers import Number
from typing import Union

def add(a: Number, b: Number) -> Union[int, float]:
    """
    Adds two numbers and returns their sum.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The sum of a and b (int or float).

    Raises:
        TypeError: If a or b are not numeric types.
    """
    ...

def subtract(a: Number, b: Number) -> Union[int, float]:
    """
    Subtracts the second number from the first and returns the difference.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The difference between a and b (int or float).

    Raises:
        TypeError: If a or b are not numeric types.
    """
    ...

def multiply(a: Number, b: Number) -> Union[int, float]:
    """
    Multiplies two numbers and returns their product.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The product of a and b (int or float).

    Raises:
        TypeError: If a or b are not numeric types.
    """
    ...

def divide(a: Number, b: Number) -> float:
    """
    Divides the first number by the second and returns the quotient.

    Args:
        a: The numerator (int or float).
        b: The denominator (int or float).

    Returns:
        The quotient of a divided by b (float).

    Raises:
        TypeError: If a or b are not numeric types.
        ZeroDivisionError: If b is zero.
    """
    ...

def power(base: Number, exponent: Number) -> Union[int, float]:
    """
    Raises the base to the power of the exponent and returns the result.

    Args:
        base: The base number (int or float).
        exponent: The exponent (int or float).

    Returns:
        The result of base raised to the power of exponent (int or float).

    Raises:
        TypeError: If base or exponent are not numeric types.
    """
    ...

def modulus(a: Number, b: Number) -> Union[int, float]:
    """
    Returns the remainder when the first number is divided by the second.

    Args:
        a: The dividend (int or float).
        b: The divisor (int or float).

    Returns:
        The remainder of a divided by b (int or float).

    Raises:
        TypeError: If a or b are not numeric types.
        ZeroDivisionError: If b is zero.
    """
    ...

def negate(a: Number) -> Union[int, float]:
    """
    Returns the negation of a number.

    Args:
        a: The number to negate (int or float).

    Returns:
        The negated number (int or float).

    Raises:
        TypeError: If a is not a numeric type.
    """
    ...
