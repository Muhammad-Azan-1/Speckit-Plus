# Data Model: Simple Calculator Library

**Branch**: `001-simple-calculator` | **Date**: 2025-11-12 | **Spec**: specs/001-simple-calculator/spec.md

## Entities

### Number

*   **Description**: Represents a numeric value used in calculations.
*   **Attributes**:
    *   `value`: The actual numeric value.
*   **Type**: Can be an integer (`int`) or a floating-point number (`float`).
*   **Constraints**:
    *   Must be a valid numeric type (int or float).
    *   Floating-point values adhere to IEEE 754 double-precision standards.

## Relationships

*   No complex relationships between entities in this simple library. Operations take one or two `Number` entities as input and return a `Number` entity.

## Validation Rules

*   **Division/Modulus by Zero**: Operations involving division or modulus where the divisor is zero will result in a `ZeroDivisionError`.
*   **Non-Numeric Input**: Operations attempted with non-numeric input types will result in a `TypeError`.
*   **Overflow/Underflow**: Handled by Python's native `float` type behavior, resulting in `inf`, `-inf`, or `0.0` as appropriate.
