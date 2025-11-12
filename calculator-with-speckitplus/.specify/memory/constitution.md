<!--
Sync Impact Report:
- Version change: 1.1.0 → 1.2.0
- Modified sections: II. Modern Python with Type Hints, Technical Stack
- Templates requiring updates: None
-->
# Calculator Project Constitution

## Core Principles

### I. Test-Driven Development
All new functionality must be accompanied by tests. The TDD (Test-Driven Development) approach is mandatory: write a failing test before writing the implementation.

### II. Modern Python with Type Hints
All Python code must be written for Python 3.14.0 and include type hints for all function signatures and variables.

### III. Clean and Readable Code
Code should be written to be easily understood by other developers. Follow standard Python style guides (PEP 8) and strive for clarity and simplicity.
- All functions must include type hints on parameters and return types
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions)
- Lines must be under 100 characters
- No magic numbers; use named constants
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`

### IV. Architectural Decision Records
Important architectural decisions must be documented in ADRs (Architectural Decision Records) to provide context and rationale for future development.

### V. SOLID, DRY, KISS Principles
Follow essential Object-Oriented Programming principles:
- **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **DRY**: Don't Repeat Yourself
- **KISS**: Keep It Simple, Stupid

## Technical Stack

- **Language**: Python 3.14.0
- **Package Manager**: UV
- **Testing Framework**: pytest
- **Version Control**: Git

## Quality Requirements

- **Tests**: All tests must pass for a build to be considered successful.
- **Code Coverage**: Maintain a minimum of 80% code coverage.
- **Data Structures**: Use dataclasses for data structures to ensure type safety and clarity.

## Governance

This constitution is the single source of truth for development standards. All code reviews and contributions must adhere to these principles. Amendments to this constitution require a pull request and approval from the project maintainers.

**Version**: 1.2.0 | **Ratified**: 2025-11-12 | **Last Amended**: 2025-11-12