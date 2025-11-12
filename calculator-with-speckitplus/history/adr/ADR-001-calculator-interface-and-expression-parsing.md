# ADR-001: Calculator Interface and Expression Parsing

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-11-12
- **Feature:** simple-calculator
- **Context:** The simple calculator library needs to define its interface for performing arithmetic operations. A key decision is whether to provide an expression parser for evaluating string-based mathematical expressions or to expose individual functions for each operation.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The library will only expose individual operation functions (e.g., `add(a, b)`, `subtract(a, b)`). It will NOT include an expression parser.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

Simpler library design and implementation, reduced development time, easier to maintain, smaller codebase. Avoids the complexity and potential security risks associated with parsing and evaluating arbitrary expressions.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Developers using the library will need to implement their own expression parsing logic if they require evaluating string-based mathematical expressions.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

**Include a basic expression parser:** This would allow users to pass full mathematical expressions as strings (e.g., "2 + 3 * 4"). Rejected due to increased complexity, potential for scope creep, and the availability of dedicated parsing libraries that can be integrated by users if needed.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/001-simple-calculator/spec.md
- Implementation Plan: specs/001-simple-calculator/plan.md
- Related ADRs: N/A
- Evaluator Evidence: history/prompts/simple-calculator/5-clarify-simple-calculator-spec.spec.prompt.md
