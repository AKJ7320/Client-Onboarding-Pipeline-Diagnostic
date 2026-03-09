# RACI Matrix — OnboardFlow Onboarding Process

**R** = Responsible (does the work) &nbsp;|&nbsp; **A** = Accountable (owns the outcome, signs off) &nbsp;|&nbsp; **C** = Consulted (provides input) &nbsp;|&nbsp; **I** = Informed (kept in the loop)

| Activity | Sales | Compliance | Operations | IT | Client |
|---|---|---|---|---|---|
| Initial application intake | R | I | I | - | R |
| KYC/AML review | I | R/A | - | - | I |
| Document collection | I | I | R | - | R |
| Compliance approval decision | I | R/A | I | - | I |
| SLA breach escalation | I | A | R | C | - |
| Funding/account activation | I | I | R/A | - | I |
| Dashboard build & maintenance | I | C | C | R/A | - |
| Monthly onboarding performance review | C | C | C | I | - |
| Process redesign sign-off (TO-BE changes) | C | A | C | C | - |

## Notes on Key Decisions
- **Compliance holds Accountability (A) for KYC/AML review and the approval decision** — this cannot shift to Ops or IT regardless of tooling, since it's a regulatory judgment call, not a process-efficiency task. Automation in this project only speeds up *routing and visibility*, never the compliance decision itself.
- **Operations owns document collection and funding execution** — these are operational/administrative, not judgment calls, and are the primary targets for the parallelization redesign (TO-BE flow).
- **IT is Accountable only for the dashboard/tooling itself**, not for the business process it reports on — a common point of confusion worth clarifying explicitly in a RACI.
