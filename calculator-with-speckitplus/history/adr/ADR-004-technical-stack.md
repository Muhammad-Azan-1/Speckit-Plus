# ADR-004: Technical Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-11-12
- **Feature:** simple-calculator
- **Context:** The project requires a defined technical stack for language, package management, testing, and version control to ensure consistency and adherence to project constitution.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The technical stack for the simple calculator library will consist of:
*   **Language**: Python 3.14.0
*   **Package Manager**: UV
*   **Testing Framework**: pytest
*   **Version Control**: Git

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

Aligns with project constitution, leverages modern and efficient tools, promotes consistent development practices, good community support for chosen tools.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Requires developers to be familiar with UV and pytest, potential learning curve for those new to these tools.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

**Package Manager: `pip`**: The standard Python package installer. Rejected in favor of `uv` due to `uv`'s superior performance and modern features, as per project constitution.
**Testing Framework: `unittest`**: Python's built-in testing framework. Rejected in favor of `pytest` due to `pytest`'s more concise syntax, powerful features, and widespread adoption in the Python community.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/001-simple-calculator/spec.md
- Implementation Plan: specs/001-simple-calculator/plan.md
- Related ADRs: N/A
- Evaluator Evidence: specs/001-simple-calculator/research.md
