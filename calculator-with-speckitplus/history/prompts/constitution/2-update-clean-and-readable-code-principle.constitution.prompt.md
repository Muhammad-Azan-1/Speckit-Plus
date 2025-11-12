---
id: 2
title: Update Clean and Readable Code Principle
stage: constitution
date: 2025-11-12
surface: agent
model: gemini
feature: none
branch: main
user: muhammadazan
command: (User provided content)
labels: ["constitution", "update"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  null
---

## Prompt

@.specify/memory/constitution.md - All functions must include type hints on parameters and return types
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions)
- Lines must be under 100 characters
- No magic numbers; use named constants
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`

## Response snapshot

The "Clean and Readable Code" principle in the constitution has been updated with more specific guidelines.

## Outcome

- ✅ Impact: Medium - Clarifies and expands on an existing principle.
- 🧪 Tests: N/A
- 📁 Files: 1 file updated
- 🔁 Next prompts: N/A
- 🧠 Reflection: The create-phr.sh script failed again. The path to the template seems to be incorrect in the script.

## Evaluation notes (flywheel)

- Failure modes observed: create-phr.sh script failed to find template.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Fix the create-phr.sh script.
