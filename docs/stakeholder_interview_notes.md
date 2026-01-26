# Stakeholder Interview Notes — Client Onboarding Efficiency Review

**Purpose:** Simulated discovery interviews conducted at project kickoff, in the style a Business Analyst would actually run before touching any data. Each stakeholder sees a different slice of the same problem — synthesizing these views into one problem statement is the first real BA task.

---

## Interview 1: Head of Client Onboarding (Process Owner)

**Key points raised:**
- "Our target is to fully onboard a retail client in 5 business days and an institutional client in 12 business days. We're missing that target more often than we used to."
- "I don't have visibility into *where* in the pipeline things slow down — I only see the final completion date, not stage-level detail."
- "I suspect month-end is worse, because my team is also pulled into monthly reporting, but I don't have data to prove it."
- **Ask:** A dashboard showing time spent at each stage, not just overall.

## Interview 2: Head of Compliance

**Key points raised:**
- "KYC/AML checks cannot be rushed — that's a regulatory non-negotiable. But some countries take disproportionately long, and I want to know if that's genuinely risk-driven or just inefficient process."
- "Rejection reasons are currently captured as free-text notes by analysts — inconsistent and hard to aggregate."
- **Ask:** Structured rejection reason tracking, and a breakdown of KYC duration by country/risk tier.

## Interview 3: Head of Retail Sales

**Key points raised:**
- "We're losing self-directed applicants during onboarding — they get frustrated and abandon the process, especially around the document upload step."
- "Institutional and commercial clients are more patient because they expect a longer process, but retail clients expect something closer to a same-day account opening."
- **Ask:** Drop-off rate by client type and stage, so we know where to fix the retail experience specifically.

## Interview 4: Onboarding Operations Manager

**Key points raised:**
- "My team of 10 handles different volumes and I think there's real variance in how fast individual agents work, but I've never measured it formally."
- "I want this to be fair to my team — I don't want a tool that just names and shames, I want to understand root causes (training gap vs. workload vs. case complexity)."
- **Ask:** Agent-level performance visibility, but paired with workload context.

---

## Synthesized Problem Statement

> Onboarding TAT (turnaround time) is missing target SLAs, and no one currently has stage-level, country-level, client-type-level, or agent-level visibility into *why*. The business needs data-driven visibility into the pipeline to distinguish genuine regulatory necessity (KYC diligence) from fixable process inefficiency (manual handoffs, sequencing, staffing gaps), so that onboarding can be sped up without compromising compliance.

## Requirements Extracted from These Interviews (feeds directly into BRD/FRD)
1. Stage-level time tracking, not just start/end dates (Head of Onboarding)
2. Month-end vs. regular-period comparison capability (Head of Onboarding)
3. Structured (not free-text) rejection reason codes (Head of Compliance)
4. Country/risk-tier level KYC duration breakdown (Head of Compliance)
5. Drop-off rate by client type and stage (Head of Retail Sales)
6. Agent-level performance view, paired with volume/workload context — not performance in isolation (Ops Manager)
