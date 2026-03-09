# User Stories — OnboardFlow
## Format: As a [role], I want [capability], so that [benefit]. Written in backlog/Jira-style with priority and acceptance criteria.

---

### US-01 (Priority: High)
**As a** Compliance Team Lead,
**I want** to see which applications have breached KYC SLA,
**so that** I can reprioritize my team's queue daily.

**Acceptance criteria:**
- Dashboard shows a filterable list of applications where KYC duration > SLA target
- List includes applicant ID, country, days overdue, assigned agent
- List updates at least daily

---

### US-02 (Priority: High)
**As a** Head of Onboarding,
**I want** a comparison of month-end vs. regular-period stage durations,
**so that** I can proactively staff up before month-end volume spikes.

**Acceptance criteria:**
- Dashboard shows average Compliance/KYC duration split by "month-end window" vs. "regular period"
- Data can be filtered by month/quarter

---

### US-03 (Priority: High)
**As a** Sales Manager,
**I want** to see drop-off rates by client type and stage,
**so that** I can identify where prospective retail clients are abandoning the process.

**Acceptance criteria:**
- Dashboard shows drop-off % per stage, filterable by client type
- Retail-specific view highlights Documentation-stage abandonment specifically

---

### US-04 (Priority: Medium)
**As a** Compliance Officer,
**I want** rejection reasons captured as structured reason codes rather than free text,
**so that** leadership can see rejection trends over time without manual text analysis.

**Acceptance criteria:**
- Rejection entry form/system restricts input to a predefined reason-code list
- Reporting can aggregate rejection counts by reason code over any date range

---

### US-05 (Priority: Medium)
**As an** Operations Director,
**I want** agent-level performance visibility paired with workload volume,
**so that** I can distinguish coaching needs from workload imbalance rather than penalizing busy agents.

**Acceptance criteria:**
- Dashboard shows agent average handling time plotted against applicant volume handled
- View is grouped/filterable by team

---

### US-06 (Priority: Medium)
**As a** Risk/Compliance Manager,
**I want** KYC duration and rejection rate broken down by country,
**so that** I can distinguish genuine risk-driven diligence from fixable process inefficiency.

**Acceptance criteria:**
- Dashboard shows average KYC duration per country
- High-friction countries are visually distinguishable (e.g., color-coded)

---

### US-07 (Priority: Low)
**As a** Client Onboarding Manager,
**I want** an automated escalation when an application exceeds SLA by more than 24 hours,
**so that** cases don't stall silently without anyone noticing.

**Acceptance criteria:**
- System sends a notification (email/dashboard alert) when the 24-hour-past-SLA threshold is crossed
- Escalation is logged with timestamp for audit purposes

---

## Backlog Summary Table

| ID | Story | Priority | Stakeholder |
|---|---|---|---|
| US-01 | KYC SLA breach visibility | High | Compliance Team Lead |
| US-02 | Month-end vs. regular comparison | High | Head of Onboarding |
| US-03 | Drop-off rate by client type/stage | High | Sales Manager |
| US-04 | Structured rejection reason codes | Medium | Compliance Officer |
| US-05 | Agent performance + workload context | Medium | Operations Director |
| US-06 | KYC duration/rejection by country | Medium | Risk/Compliance Manager |
| US-07 | Automated SLA breach escalation | Low | Client Onboarding Manager |
