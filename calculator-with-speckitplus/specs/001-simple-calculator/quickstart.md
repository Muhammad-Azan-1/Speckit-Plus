# Quickstart Guide: Simple Calculator Library

**Branch**: `001-simple-calculator` | **Date**: 2025-11-12 | **Spec**: specs/001-simple-calculator/spec.md

This guide provides a quick overview of how to install and use the Simple Calculator Library.

## Installation

Assuming you have `uv` installed, you can install the library (once published) using:

```bash
uv pip install simple-calculator
```

## Usage

The library exposes individual functions for each arithmetic operation.

### Basic Arithmetic Operations

```python
from simple_calculator import add, subtract, multiply, divide, power, modulus, negate

# Addition
result_add = add(10, 5)
print(f"10 + 5 = {result_add}")  # Output: 15

# Subtraction
result_subtract = subtract(10, 5)
print(f"10 - 5 = {result_subtract}")  # Output: 5

# Multiplication
result_multiply = multiply(10, 5)
print(f"10 * 5 = {result_multiply}") # Output: 50

# Division
result_divide = divide(10, 5)
print(f"10 / 5 = {result_divide}")  # Output: 2.0

# Exponentiation
result_power = power(2, 3)
print(f"2 ** 3 = {result_power}")   # Output: 8

# Modulus
result_modulus = modulus(10, 3)
print(f"10 % 3 = {result_modulus}") # Output: 1

# Negation
result_negate = negate(7)
print(f"-7 = {result_negate}")      # Output: -7
```

### Error Handling

The library raises standard Python exceptions for invalid operations:

```python
from simple_calculator import divide

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}") # Output: Error: division by zero

from simple_calculator import add

try:
    result = add(10, "five")
except TypeError as e:
    print(f"Error: {e}") # Output: Error: unsupported operand type(s) for +: 'int' and 'str'
```
