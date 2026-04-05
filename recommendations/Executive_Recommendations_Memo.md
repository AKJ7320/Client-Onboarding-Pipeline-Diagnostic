# Executive Recommendations Memo
## OnboardFlow: Client Onboarding Efficiency Analysis

**To:** Head of Client Onboarding, Head of Compliance, Head of Retail Sales, Operations Director
**From:** Business Analyst, Onboarding Efficiency Project
**Re:** Findings and recommended actions from the onboarding pipeline diagnostic

---

## 1. Summary

Over the past several weeks, we analyzed the end-to-end client onboarding pipeline — from application submission through first trade — across 3,000 applicants spanning Institutional, Commercial, and Retail client segments. The objective was to identify *why* onboarding TAT (turnaround time) has been missing SLA targets, using stage-level pipeline data rather than relying on the final completion date alone.

We found four distinct, addressable root causes, each backed by SQL analysis, exploratory data visualization, and a live monitoring dashboard. None of these require relaxing KYC/AML regulatory standards — every recommendation targets process inefficiency, not compliance rigor.

**Overall completion rate: 83%.** **Compliance is the single slowest and most SLA-breached stage** in the pipeline (42% breach rate).

---

## 2. Key Findings

### Finding 1: Month-end submissions take significantly longer at Compliance
Applications submitted in the last 5 days of any month take **2.80 additional days** on average to clear the Compliance stage compared to regular-period submissions. This pattern recurs consistently across the full 15-month dataset (visible in the Compliance Duration Trend chart), indicating a structural staffing/capacity issue tied to month-end reporting workload — not a one-off anomaly.

### Finding 2: KYC duration is disproportionately high for 4 countries
Applicants from Nigeria, Pakistan, Russia, and UAE experience KYC durations of **5.2 to 6.4 days on average**, more than double the ~2.5-2.8 day average seen across the other 7 countries in our dataset. This may reflect legitimate risk-based diligence — but the magnitude and consistency of the gap warrants a joint review with Compliance to separate genuine regulatory necessity from fixable process inefficiency.

### Finding 3: Retail clients abandon the Documentation stage at nearly 3x the rate of other segments
**11% of Retail applicants drop off at the Documentation stage**, compared to 1.7% (Institutional) and 2.9% (Commercial). This is the single largest point of client loss in the entire funnel, and — unlike Findings 1 and 2 — it is entirely within our control, since it reflects the self-serve document upload experience rather than external risk factors.

### Finding 4: Two onboarding agents show a persistent performance gap unrelated to workload
Across our 13-agent onboarding team, average stage-handling time ranges from **0.97 to 3.73 days**, a gap of **2.76 days**. Critically, the two slowest agents (Noah Rhodes, Institutional; Ryan Munoz, Retail) are *not* the highest-volume agents on their teams — ruling out workload as the explanation, and pointing instead toward a training or process-adherence gap.

---

## 3. Recommendations

| # | Recommendation | Target Finding | Expected Impact |
|---|---|---|---|
| 1 | Introduce month-end capacity smoothing: pre-allocate additional Compliance reviewers or temporarily redistribute non-urgent reviews in the 5 business days before month-end. | Finding 1 | Reduce month-end Compliance delay from ~2.8 days toward the regular-period baseline (~1.5-2 days) |
| 2 | Conduct a joint Compliance/Ops review of the 4 high-friction countries to distinguish genuine risk-based diligence from process inefficiency (e.g., manual database cross-checks that could be automated). | Finding 2 | Potential to cut KYC duration for these countries by 30-50% without reducing diligence quality |
| 3 | Redesign the Retail document upload experience: parallelize document collection with KYC initiation (per the TO-BE process flow) rather than requesting documents only after KYC begins, and add proactive reminders/support during the upload window. | Finding 3 | Reduce Retail Documentation drop-off from 11% toward Institutional/Commercial levels (~2-3%), meaningfully improving overall completion rate |
| 4 | Pair the two flagged agents with a peer mentor for their next onboarding cohort and re-measure handling time after 30 days to confirm improvement before considering further action. | Finding 4 | Close some or all of the 2.76-day performance gap; low-cost, non-punitive first intervention |

## 4. Suggested Next Steps
1. Socialize these findings with the 4 stakeholder groups interviewed at project kickoff (see `stakeholder_interview_notes.md`).
2. Prioritize Recommendation 3 (Retail Documentation redesign) first — it is fully within Ops/Product control, requires no Compliance sign-off, and targets the single largest completion-rate lever.
3. Establish the Power BI dashboard built in this project as an ongoing monitoring tool, reviewed monthly by the Head of Onboarding, rather than a one-time analysis.
4. Revisit Finding 2 (country-level KYC friction) specifically with Compliance leadership before making any process changes, given its regulatory sensitivity.

## 5. Methodology Note
This analysis used a synthetic dataset (3,000 applicants, 15-month window) constructed to reflect realistic onboarding pipeline dynamics for a multi-asset brokerage. Findings and magnitudes are illustrative of the analytical approach; a production deployment would validate these specific root causes against live operational data before final action.
