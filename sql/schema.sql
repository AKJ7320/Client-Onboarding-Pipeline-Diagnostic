-- ============================================================
-- schema.sql
-- Creates the OnboardFlow database and all 5 tables.
-- Column names/types match the CSVs produced by
-- data_generation/generate_synthetic_data.py exactly.
-- ============================================================

CREATE DATABASE IF NOT EXISTS onboardflow_db;
USE onboardflow_db;

-- Drop tables if re-running this script (clean slate)
DROP TABLE IF EXISTS rejections;
DROP TABLE IF EXISTS pipeline_stages;
DROP TABLE IF EXISTS applicants;
DROP TABLE IF EXISTS sla_targets;
DROP TABLE IF EXISTS agents;

-- ------------------------------------------------------------
-- agents: the 13 onboarding agents across 3 teams
-- ------------------------------------------------------------
CREATE TABLE agents (
    agent_id   INT PRIMARY KEY,
    agent_name VARCHAR(100),
    team       VARCHAR(50),
    region     VARCHAR(50)
);

-- ------------------------------------------------------------
-- sla_targets: target days per stage, per client type
-- Composite primary key since a (stage, client_type) pair is unique
-- ------------------------------------------------------------
CREATE TABLE sla_targets (
    stage_name  VARCHAR(30),
    client_type VARCHAR(20),
    target_days INT,
    PRIMARY KEY (stage_name, client_type)
);

-- ------------------------------------------------------------
-- applicants: one row per applicant
-- ------------------------------------------------------------
CREATE TABLE applicants (
    applicant_id       INT PRIMARY KEY,
    client_type        VARCHAR(20),
    country             VARCHAR(50),
    channel             VARCHAR(30),
    submitted_date      DATE,
    onboarding_agent_id INT,
    final_status        VARCHAR(20),
    FOREIGN KEY (onboarding_agent_id) REFERENCES agents(agent_id)
);

-- ------------------------------------------------------------
-- pipeline_stages: one row per (applicant, stage) — the core table
-- stage_end is NULL when the applicant dropped off at that stage
-- ------------------------------------------------------------
CREATE TABLE pipeline_stages (
    stage_id        INT PRIMARY KEY,
    applicant_id    INT,
    stage_name      VARCHAR(30),
    stage_start     DATETIME,
    stage_end       DATETIME NULL,
    sla_target_days INT,
    stage_status    VARCHAR(20),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- ------------------------------------------------------------
-- rejections: only exists for applicants dropped at Compliance stage
-- ------------------------------------------------------------
CREATE TABLE rejections (
    rejection_id  INT PRIMARY KEY,
    applicant_id  INT,
    stage_name    VARCHAR(30),
    reason_desc   VARCHAR(200),
    rejected_date DATE,
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Helpful indexes for the analysis queries we'll run in Part 3
CREATE INDEX idx_stages_applicant ON pipeline_stages(applicant_id);
CREATE INDEX idx_stages_name ON pipeline_stages(stage_name);
CREATE INDEX idx_applicants_type ON applicants(client_type);
CREATE INDEX idx_applicants_country ON applicants(country);

USE onboardflow_db;
SELECT COUNT(*) FROM applicants;
SELECT stage_name, COUNT(*) FROM pipeline_stages GROUP BY stage_name;