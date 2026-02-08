-- ============================================================
-- analysis_queries.sql
-- Core BA analysis queries for OnboardFlow
-- Run these one at a time in MySQL Workbench (highlight a query,
-- press Ctrl+Enter) so you can read each result before moving on.
-- ============================================================

USE onboardflow_db;

-- ------------------------------------------------------------
-- QUERY 1: Average time-in-stage, per stage
-- Purpose: answers the Head of Onboarding's #1 ask — "where does
-- time actually go in the pipeline?"
-- ------------------------------------------------------------
SELECT
    stage_name,
    ROUND(AVG(TIMESTAMPDIFF(HOUR, stage_start, stage_end)) / 24.0, 2) AS avg_days_in_stage,
    COUNT(*) AS completed_count
FROM pipeline_stages
WHERE stage_status = 'Completed'
GROUP BY stage_name
ORDER BY avg_days_in_stage DESC;


-- ------------------------------------------------------------
-- QUERY 2: SLA breach rate by stage and client type
-- Purpose: quantifies how often we miss our own committed SLA
-- (from the BRD), broken down by client segment
-- ------------------------------------------------------------
SELECT
    p.stage_name,
    a.client_type,
    COUNT(*) AS total,
    SUM(CASE WHEN TIMESTAMPDIFF(DAY, p.stage_start, p.stage_end) > p.sla_target_days THEN 1 ELSE 0 END) AS breaches,
    ROUND(100.0 * SUM(CASE WHEN TIMESTAMPDIFF(DAY, p.stage_start, p.stage_end) > p.sla_target_days THEN 1 ELSE 0 END) / COUNT(*), 1) AS breach_pct
FROM pipeline_stages p
JOIN applicants a ON p.applicant_id = a.applicant_id
WHERE p.stage_status = 'Completed'
GROUP BY p.stage_name, a.client_type
ORDER BY breach_pct DESC;


-- ------------------------------------------------------------
-- QUERY 3: Drop-off rate by stage
-- Purpose: identifies WHERE in the funnel applicants abandon
-- ------------------------------------------------------------
SELECT
    stage_name,
    COUNT(*) AS total,
    SUM(CASE WHEN stage_status = 'Dropped' THEN 1 ELSE 0 END) AS dropped,
    ROUND(100.0 * SUM(CASE WHEN stage_status = 'Dropped' THEN 1 ELSE 0 END) / COUNT(*), 1) AS drop_pct
FROM pipeline_stages
GROUP BY stage_name
ORDER BY drop_pct DESC;


-- ------------------------------------------------------------
-- QUERY 4: ROOT CAUSE 3 — Drop-off rate at Documentation stage,
-- split by client type (tests: is Retail really worse?)
-- ------------------------------------------------------------
SELECT
    a.client_type,
    COUNT(*) AS total_at_stage,
    SUM(CASE WHEN p.stage_status = 'Dropped' THEN 1 ELSE 0 END) AS dropped,
    ROUND(100.0 * SUM(CASE WHEN p.stage_status = 'Dropped' THEN 1 ELSE 0 END) / COUNT(*), 1) AS drop_pct
FROM pipeline_stages p
JOIN applicants a ON p.applicant_id = a.applicant_id
WHERE p.stage_name = 'Documentation'
GROUP BY a.client_type
ORDER BY drop_pct DESC;


-- ------------------------------------------------------------
-- QUERY 5: ROOT CAUSE 1 — Month-end effect on Compliance stage
-- Purpose: tests the Head of Onboarding's suspicion that month-end
-- reporting workload slows down Compliance approvals
-- ------------------------------------------------------------
SELECT
    CASE WHEN DAY(a.submitted_date) >= 26 THEN 'Month-End (26-31)' ELSE 'Regular Period' END AS submission_window,
    COUNT(*) AS total,
    ROUND(AVG(TIMESTAMPDIFF(HOUR, p.stage_start, p.stage_end)) / 24.0, 2) AS avg_days
FROM pipeline_stages p
JOIN applicants a ON p.applicant_id = a.applicant_id
WHERE p.stage_name = 'Compliance' AND p.stage_status = 'Completed'
GROUP BY submission_window;


-- ------------------------------------------------------------
-- QUERY 6: ROOT CAUSE 2 — KYC duration by country
-- Purpose: tests the Head of Compliance's question — is delay
-- genuinely risk-driven, or just inefficiency?
-- ------------------------------------------------------------
SELECT
    a.country,
    COUNT(*) AS total,
    ROUND(AVG(TIMESTAMPDIFF(HOUR, p.stage_start, p.stage_end)) / 24.0, 2) AS avg_kyc_days
FROM pipeline_stages p
JOIN applicants a ON p.applicant_id = a.applicant_id
WHERE p.stage_name = 'KYC' AND p.stage_status = 'Completed'
GROUP BY a.country
ORDER BY avg_kyc_days DESC;


-- ------------------------------------------------------------
-- QUERY 7: ROOT CAUSE 4 — Agent performance ranking
-- Purpose: the Ops Manager's ask — agent-level visibility,
-- paired with volume so it's fair (not just "who's slowest")
-- Uses a window function (RANK) — a good SQL skill to show off
-- ------------------------------------------------------------
SELECT
    ag.agent_name,
    ag.team,
    COUNT(DISTINCT p.applicant_id) AS applicants_handled,
    ROUND(AVG(TIMESTAMPDIFF(HOUR, p.stage_start, p.stage_end)) / 24.0, 2) AS avg_days_per_stage,
    RANK() OVER (PARTITION BY ag.team ORDER BY AVG(TIMESTAMPDIFF(HOUR, p.stage_start, p.stage_end)) DESC) AS slowness_rank_in_team
FROM pipeline_stages p
JOIN applicants a ON p.applicant_id = a.applicant_id
JOIN agents ag ON a.onboarding_agent_id = ag.agent_id
WHERE p.stage_status = 'Completed'
GROUP BY ag.agent_id, ag.agent_name, ag.team
ORDER BY ag.team, slowness_rank_in_team;


-- ------------------------------------------------------------
-- QUERY 8: Top rejection reasons
-- Purpose: the Head of Compliance's ask for structured
-- (not free-text) rejection reason tracking
-- ------------------------------------------------------------
SELECT
    reason_desc,
    COUNT(*) AS occurrences,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM rejections), 1) AS pct_of_all_rejections
FROM rejections
GROUP BY reason_desc
ORDER BY occurrences DESC;


-- ------------------------------------------------------------
-- QUERY 9: Overall funnel — how many applicants reach each stage
-- Purpose: the headline funnel visual for the Executive Summary
-- dashboard page
-- ------------------------------------------------------------
SELECT
    stage_name,
    COUNT(*) AS applicants_reaching_stage
FROM pipeline_stages
GROUP BY stage_name
ORDER BY FIELD(stage_name, 'Application','KYC','Documentation','Compliance','Funding','FirstTrade');


-- ------------------------------------------------------------
-- QUERY 10: Overall completion rate and average end-to-end TAT
-- Purpose: the single most important KPI in the BRD's Success Metrics
-- ------------------------------------------------------------
SELECT
    a.client_type,
    COUNT(*) AS total_applicants,
    SUM(CASE WHEN a.final_status = 'Completed' THEN 1 ELSE 0 END) AS completed,
    ROUND(100.0 * SUM(CASE WHEN a.final_status = 'Completed' THEN 1 ELSE 0 END) / COUNT(*), 1) AS completion_rate_pct
FROM applicants a
GROUP BY a.client_type;
