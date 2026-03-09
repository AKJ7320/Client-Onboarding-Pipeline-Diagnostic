# Functional Requirements Document (FRD)
## Project: OnboardFlow — Client Onboarding Efficiency Analysis

**Related Documents:** `BRD_OnboardFlow.md`, `AS_IS_process_flow.png`, `TO_BE_process_flow.png`

This FRD translates the BRD's business objectives into specific, testable functional requirements for a future onboarding monitoring/alerting system (beyond the diagnostic dashboard already built in this project).

---

## 1. Functional Requirements

| ID | Requirement | Source (traces to stakeholder ask) |
|---|---|---|
| FR1 | System shall automatically flag any application exceeding its stage SLA by more than 24 hours and notify the assigned agent's team lead. | Head of Onboarding — stage-level visibility |
| FR2 | System shall provide a dashboard segmented by client type, country, and pipeline stage, refreshed at least daily. | Head of Onboarding — stage-level visibility |
| FR3 | System shall capture rejection reasons using a structured, predefined reason-code list (not free text). | Head of Compliance — structured rejection tracking |
| FR4 | System shall report KYC stage duration and rejection rate broken down by country/risk tier. | Head of Compliance — country-level view |
| FR5 | System shall report drop-off rate by pipeline stage, segmented by client type. | Head of Retail Sales — drop-off visibility |
| FR6 | System shall provide agent-level performance metrics (average handling time, volume) alongside team benchmarks, to enable fair comparison. | Ops Manager — agent visibility with context |
| FR7 | System shall flag submission-volume patterns (e.g., month-end spikes) to support proactive staffing decisions. | Head of Onboarding — month-end concern |
| FR8 | System shall support parallel initiation of KYC and Documentation collection stages (rather than strictly sequential), where compliance rules permit. | Process redesign (TO-BE flow) |

## 2. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR1 | Dashboard shall refresh within 15 minutes of underlying data load completing. |
| NFR2 | Role-based access: Compliance roles see full rejection detail; Sales roles see funnel/volume metrics only (no PII/rejection detail). |
| NFR3 | System shall retain historical onboarding data for a minimum of 24 months to support trend analysis. |
| NFR4 | All automated alerts/escalations shall be logged with timestamp and recipient for audit purposes. |

## 3. Out of Scope (explicitly, to prevent scope creep)
- Automating the KYC/AML decision itself (regulatory judgment remains human-owned)
- Changes to underlying regulatory requirements
- Marketing/lead-generation funnel prior to application submission
- Post-onboarding account servicing workflows

## 4. Acceptance Criteria (sample, for FR1)
- **Given** an application's KYC stage has been open for more than (SLA target + 24 hours),
- **When** the daily monitoring job runs,
- **Then** the assigned agent's team lead receives a notification listing the applicant ID, stage, and hours overdue.
