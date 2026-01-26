# Business Requirements Document (BRD)
## Project: OnboardFlow — Client Onboarding Efficiency Analysis

**Document Owner:** Business Analyst
**Status:** Draft for Stakeholder Sign-off
**Related Document:** `stakeholder_interview_notes.md`

---

## 1. Business Objective
Reduce average client onboarding turnaround time (TAT) and improve pipeline completion rate, without compromising KYC/AML compliance standards, by identifying and addressing the specific root causes of delay across the onboarding pipeline.

## 2. Background / Problem Statement
The onboarding pipeline (Application → KYC/AML → Documentation → Compliance Approval → Funding → First Trade) is missing internally set SLA targets (5 business days for retail clients, 12 for institutional). Leadership currently only has visibility into total onboarding time, not stage-level performance, which prevents targeted intervention. Anecdotal concerns exist around month-end capacity strain, country-specific KYC delays, and retail client drop-off during document submission, but none of this is currently quantified.

## 3. Scope

**In scope:**
- Onboarding pipeline from initial application through first trade execution
- All three client segments: Institutional, Commercial, Retail
- Stage-level time tracking, drop-off analysis, SLA compliance measurement, rejection reason analysis, agent performance visibility

**Out of scope:**
- Post-onboarding account servicing or trading activity
- Marketing/lead generation funnel (pre-application)
- Any changes to regulatory KYC/AML requirements themselves

## 4. Stakeholders

| Stakeholder | Interest |
|---|---|
| Head of Client Onboarding | Owns overall TAT target; needs stage-level visibility |
| Head of Compliance | Owns KYC/AML process; needs structured rejection data and country-level view |
| Head of Retail Sales | Owns client acquisition; needs drop-off visibility by segment |
| Onboarding Operations Manager | Owns agent team performance; needs fair, context-aware visibility |
| IT/Data (implied) | Would own any future system implementation |

## 5. Assumptions & Constraints
- Regulatory KYC/AML requirements are fixed and cannot be shortened — only process inefficiency around them can be targeted.
- Analysis assumes current staffing levels unless a specific reallocation recommendation is made.
- This phase is a diagnostic/analytics project; it does not include building or deploying a live production system, only a monitoring dashboard and recommendations.

## 6. Success Metrics (tie directly to KPIs in Section 7)
- Reduce average end-to-end onboarding TAT by a target of ~25%
- Improve overall pipeline completion rate (reduce drop-off) by 10 percentage points
- Achieve >90% SLA compliance at each pipeline stage
- Reduce KYC-stage duration variance across countries where not risk-justified

## 7. Key Performance Indicators to be Reported
1. Average time-in-stage (days), per stage
2. SLA breach rate (%), per stage and client type
3. Drop-off / abandonment rate (%), per stage and client type
4. KYC duration and rejection rate, by country
5. Agent-level average handling time and applicant volume
6. Month-end vs. regular-period stage duration comparison

## 8. Deliverables
- Stage-level onboarding pipeline dataset and data model
- SQL-based analysis of bottlenecks, SLA breaches, and drop-off patterns
- Power BI dashboard for ongoing monitoring
- AS-IS and TO-BE process flow diagrams
- Functional Requirements Document (FRD) for a proposed future monitoring/alerting system
- Executive recommendations memo

## 9. Sign-off (simulated)
| Role | Name (placeholder) | Status |
|---|---|---|
| Head of Client Onboarding | — | Pending |
| Head of Compliance | — | Pending |
| Head of Retail Sales | — | Pending |
