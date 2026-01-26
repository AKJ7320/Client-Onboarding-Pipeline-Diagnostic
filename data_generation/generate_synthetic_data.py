"""
generate_synthetic_data.py
---------------------------
Generates synthetic client onboarding pipeline data for the OnboardFlow project.

Run this script from the PROJECT ROOT folder (onboardflow/), e.g.:
    python data_generation/generate_synthetic_data.py

Produces 5 CSV files inside data/:
    - agents.csv
    - applicants.csv
    - pipeline_stages.csv
    - rejections.csv
    - sla_targets.csv

Deliberately encodes four root causes for later discovery via SQL/Python analysis:
    1. Month-end KYC/Compliance slowdown
    2. Country-specific KYC friction
    3. Client-type-driven drop-off divergence (Retail abandons more at Documentation)
    4. Agent performance variance (2 "slow" agents out of 13)
"""

import random
import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

# ---------- REPRODUCIBILITY ----------
# Fixing the random seed means anyone who runs this script gets the EXACT
# same dataset every time. This matters for a portfolio project: your
# screenshots, SQL results, and findings will always match what a recruiter
# gets if they clone and run your repo themselves.
random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

# ---------- CONFIG ----------
NUM_APPLICANTS = 3000
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 3, 31)

CLIENT_TYPES = ["Institutional", "Commercial", "Retail"]
CLIENT_TYPE_WEIGHTS = [0.15, 0.20, 0.65]  # retail is highest volume, realistic for a brokerage

CHANNELS = ["Direct", "Referral", "Online Signup"]

LOW_FRICTION_COUNTRIES = ["USA", "UK", "Germany", "Singapore", "India", "Canada", "Australia"]
HIGH_FRICTION_COUNTRIES = ["Nigeria", "Pakistan", "Russia", "UAE"]
ALL_COUNTRIES = LOW_FRICTION_COUNTRIES + HIGH_FRICTION_COUNTRIES
COUNTRY_WEIGHTS = [0.15, 0.15, 0.10, 0.08, 0.15, 0.07, 0.05] + [0.10, 0.06, 0.05, 0.04]

STAGES = ["Application", "KYC", "Documentation", "Compliance", "Funding", "FirstTrade"]

# Base stage duration in days: (mean, std_dev), per (client_type, stage)
# Institutional = slower but more thorough; Retail = faster baseline
BASE_DURATION = {
    ("Institutional", "Application"): (0, 0),
    ("Institutional", "KYC"): (3, 0.5),
    ("Institutional", "Documentation"): (4, 1),
    ("Institutional", "Compliance"): (3, 0.5),
    ("Institutional", "Funding"): (2, 0.5),
    ("Institutional", "FirstTrade"): (1, 0.3),

    ("Commercial", "Application"): (0, 0),
    ("Commercial", "KYC"): (2.5, 0.5),
    ("Commercial", "Documentation"): (3, 1),
    ("Commercial", "Compliance"): (2.5, 0.5),
    ("Commercial", "Funding"): (1.5, 0.5),
    ("Commercial", "FirstTrade"): (1, 0.3),

    ("Retail", "Application"): (0, 0),
    ("Retail", "KYC"): (1.5, 0.4),
    ("Retail", "Documentation"): (1, 0.4),
    ("Retail", "Compliance"): (1, 0.3),
    ("Retail", "Funding"): (0.5, 0.2),
    ("Retail", "FirstTrade"): (0.5, 0.2),
}

# SLA targets in days, per client type per stage (from the BRD)
SLA_TARGET = {
    "Institutional": {"KYC": 3, "Documentation": 4, "Compliance": 3, "Funding": 2, "FirstTrade": 1},
    "Commercial":    {"KYC": 2, "Documentation": 3, "Compliance": 2, "Funding": 2, "FirstTrade": 1},
    "Retail":        {"KYC": 1, "Documentation": 1, "Compliance": 1, "Funding": 1, "FirstTrade": 1},
}

# Root cause 3: drop-off probability per stage per client type
DROPOFF_PROB = {
    "Institutional": {"KYC": 0.01, "Documentation": 0.02, "Compliance": 0.02, "Funding": 0.01, "FirstTrade": 0.01},
    "Commercial":    {"KYC": 0.02, "Documentation": 0.03, "Compliance": 0.03, "Funding": 0.01, "FirstTrade": 0.01},
    "Retail":        {"KYC": 0.03, "Documentation": 0.12, "Compliance": 0.05, "Funding": 0.02, "FirstTrade": 0.02},
}

REJECTION_REASONS = [
    "Incomplete ID document",
    "Proof of address mismatch",
    "Source of funds unclear",
    "Sanctions list match - manual review",
    "Duplicate application",
]


def is_month_end(d):
    """Simple heuristic: last 5 calendar days of any month = month-end window."""
    return d.day >= 26


def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))


# ---------- STEP 1: GENERATE AGENTS ----------
teams = {
    "Institutional": "Institutional Onboarding",
    "Commercial": "Commercial Onboarding",
    "Retail": "Retail Onboarding",
}

agents = []
agent_id = 1
for client_type, team_name in teams.items():
    n_agents = 5 if client_type == "Retail" else 4  # retail team is biggest (highest volume)
    for _ in range(n_agents):
        agents.append({
            "agent_id": agent_id,
            "agent_name": fake.name(),
            "team": team_name,
            "region": random.choice(["North America", "Europe", "APAC"]),
        })
        agent_id += 1

agents_df = pd.DataFrame(agents)

# Root cause 4: mark exactly 2 agents as "slow" (out of 13 total)
SLOW_AGENT_IDS = set(random.sample(list(agents_df["agent_id"]), 2))
print(f"Slow agents (for later discovery): {sorted(SLOW_AGENT_IDS)}")

# ---------- STEP 2: GENERATE APPLICANTS + PIPELINE STAGES ----------
applicants = []
stage_rows = []
rejection_rows = []
stage_id_counter = 1
rejection_id_counter = 1

for applicant_id in range(1, NUM_APPLICANTS + 1):
    client_type = random.choices(CLIENT_TYPES, weights=CLIENT_TYPE_WEIGHTS)[0]
    country = random.choices(ALL_COUNTRIES, weights=COUNTRY_WEIGHTS)[0]
    channel = random.choice(CHANNELS)
    submitted_date = random_date(START_DATE, END_DATE)

    team_name = teams[client_type]
    possible_agents = agents_df.loc[agents_df["team"] == team_name, "agent_id"].tolist()
    assigned_agent_id = random.choice(possible_agents)

    month_end_flag = is_month_end(submitted_date)
    country_friction = country in HIGH_FRICTION_COUNTRIES
    agent_is_slow = assigned_agent_id in SLOW_AGENT_IDS

    current_time = datetime.combine(submitted_date, datetime.min.time()) + timedelta(
        hours=random.randint(8, 17)
    )
    final_status = "Completed"

    for stage in STAGES:
        mean, std = BASE_DURATION[(client_type, stage)]
        duration_days = max(0.05, np.random.normal(mean, std))

        # Root cause 1: month-end backlog hits KYC and Compliance specifically
        if month_end_flag and stage in ("KYC", "Compliance"):
            duration_days *= random.uniform(2.0, 3.0)

        # Root cause 2: high-friction countries hit KYC specifically
        if country_friction and stage == "KYC":
            duration_days *= random.uniform(1.8, 2.5)

        # Root cause 4: slow agents affect the human-touched stages
        if agent_is_slow and stage in ("KYC", "Documentation", "Compliance"):
            duration_days *= random.uniform(1.4, 1.6)

        stage_start = current_time
        stage_end = stage_start + timedelta(days=duration_days)
        sla_target = SLA_TARGET.get(client_type, {}).get(stage, 0)

        # Root cause 3: drop-off probability (never at Application stage)
        dropoff_p = DROPOFF_PROB.get(client_type, {}).get(stage, 0)
        will_drop = stage != "Application" and random.random() < dropoff_p

        if will_drop:
            stage_rows.append({
                "stage_id": stage_id_counter,
                "applicant_id": applicant_id,
                "stage_name": stage,
                "stage_start": stage_start,
                "stage_end": None,
                "sla_target_days": sla_target,
                "stage_status": "Dropped",
            })
            stage_id_counter += 1
            final_status = "Dropped"

            if stage == "Compliance":
                if country_friction:
                    reason = random.choices(
                        REJECTION_REASONS, weights=[0.15, 0.15, 0.25, 0.30, 0.15]
                    )[0]
                else:
                    reason = random.choice(REJECTION_REASONS)
                rejection_rows.append({
                    "rejection_id": rejection_id_counter,
                    "applicant_id": applicant_id,
                    "stage_name": stage,
                    "reason_desc": reason,
                    "rejected_date": stage_start.date(),
                })
                rejection_id_counter += 1
            break
        else:
            stage_rows.append({
                "stage_id": stage_id_counter,
                "applicant_id": applicant_id,
                "stage_name": stage,
                "stage_start": stage_start,
                "stage_end": stage_end,
                "sla_target_days": sla_target,
                "stage_status": "Completed",
            })
            stage_id_counter += 1
            current_time = stage_end

    applicants.append({
        "applicant_id": applicant_id,
        "client_type": client_type,
        "country": country,
        "channel": channel,
        "submitted_date": submitted_date.date(),
        "onboarding_agent_id": assigned_agent_id,
        "final_status": final_status,
    })

applicants_df = pd.DataFrame(applicants)
stages_df = pd.DataFrame(stage_rows)
rejections_df = pd.DataFrame(rejection_rows)

sla_rows = [
    {"stage_name": stage, "client_type": ct, "target_days": target}
    for ct, stage_dict in SLA_TARGET.items()
    for stage, target in stage_dict.items()
]
sla_df = pd.DataFrame(sla_rows)

# ---------- STEP 3: SAVE TO CSV ----------
os.makedirs("data", exist_ok=True)
agents_df.to_csv("data/agents.csv", index=False)
applicants_df.to_csv("data/applicants.csv", index=False)
stages_df.to_csv("data/pipeline_stages.csv", index=False)
rejections_df.to_csv("data/rejections.csv", index=False)
sla_df.to_csv("data/sla_targets.csv", index=False)

# ---------- STEP 4: QUICK SANITY CHECK PRINTOUT ----------
print("\n--- Generation complete ---")
print(f"Agents:          {len(agents_df)}")
print(f"Applicants:      {len(applicants_df)}")
print(f"Pipeline stages: {len(stages_df)}")
print(f"Rejections:      {len(rejections_df)}")
print(f"\nFinal status breakdown:\n{applicants_df['final_status'].value_counts()}")
print(f"\nClient type breakdown:\n{applicants_df['client_type'].value_counts()}")
