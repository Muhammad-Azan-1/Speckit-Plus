# ADR-002: Floating-Point Precision

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-11-12
- **Feature:** simple-calculator
- **Context:** The simple calculator library needs to define its approach to handling floating-point numbers and their precision.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The library will utilize Python's native `float` type for all floating-point calculations, which adheres to IEEE 754 double-precision standards.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

Simplicity of implementation, leverages built-in language features, sufficient precision for general-purpose calculations, good performance.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Inherits the known limitations of binary floating-point arithmetic (e.g., inability to represent some decimal fractions exactly), which might lead to unexpected results in specific scenarios (e.g., financial calculations requiring exact decimal representation).

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

**Using Python's `decimal` module:** This would provide arbitrary-precision decimal arithmetic. Rejected due to increased complexity, potential performance overhead, and the fact that the "simple calculator" context does not explicitly require such high precision.

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
