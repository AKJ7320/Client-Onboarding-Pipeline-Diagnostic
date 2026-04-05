# OnboardFlow — Client Onboarding Efficiency Analysis

A full Business Analyst project simulating a client onboarding pipeline diagnostic for a multi-asset brokerage (institutional, commercial/commodity, and retail clients) — built end-to-end from requirements gathering through executive recommendations.

**[Read the full Executive Recommendations Memo →](recommendations/Executive_Recommendations_Memo.md)**

---

## The Business Problem

A brokerage's client onboarding pipeline (Application → KYC/AML → Documentation → Compliance Approval → Funding → First Trade) was missing internal SLA targets, and leadership had no stage-level visibility into *why*. This project diagnoses the root causes using SQL, Python, and Power BI — then translates findings into a formal BRD/FRD, process redesign, and executive recommendations memo.

## Key Findings

- **Month-end submissions take 2.80 additional days** at the Compliance stage — a recurring, structural staffing pattern, not random noise
- **4 countries show KYC durations 2x+ higher** than the rest of the dataset — a candidate for review with Compliance
- **Retail clients abandon the Documentation stage at ~11%**, nearly 3x the rate of Institutional/Commercial clients — the single largest fixable point of client loss
- **2 of 13 onboarding agents show a 2.76-day performance gap** unrelated to workload volume — a coaching opportunity, not a staffing one

## Dashboard Preview

*(4-page Power BI dashboard: Executive Summary, Bottleneck Deep-Dive, Segment & Geography, Operations & Agent Performance — see `powerbi/OnboardFlow_Dashboard.pbix`)*

## Tech Stack

- **Python** (pandas, numpy, Faker, matplotlib, seaborn) — synthetic data generation and exploratory analysis
- **MySQL** — relational data model and SQL analysis
- **Power BI** — 4-page interactive dashboard with DAX measures
- **Excel** — supplementary reporting
- **Git/GitHub** — version control

## Project Structure

```
onboardflow/
├── docs/                          # BA documentation
│   ├── BRD_OnboardFlow.md
│   ├── FRD_OnboardFlow.md
│   ├── stakeholder_interview_notes.md
│   ├── User_Stories.md
│   ├── RACI_Matrix.md
│   ├── AS_IS_process_flow.png
│   └── TO_BE_process_flow.png
├── data_generation/
│   └── generate_synthetic_data.py # Synthetic dataset generator (seeded, reproducible)
├── data/                          # Generated CSVs
├── sql/
│   ├── schema.sql                 # Database schema
│   ├── load_data_to_mysql.py      # Data loader
│   ├── db_config_template.py      # Config template (copy to db_config.py with your own credentials)
│   └── analysis_queries.sql       # 10 core analysis queries
├── notebooks/
│   └── onboardflow_analysis.ipynb # Exploratory analysis with 5 visualizations
├── powerbi/
│   └── OnboardFlow_Dashboard.pbix # 4-page interactive dashboard
├── recommendations/
│   └── Executive_Recommendations_Memo.md
└── requirements.txt
```

## How to Reproduce This Project

1. Clone this repo and set up a Python virtual environment: `pip install -r requirements.txt`
2. Generate the synthetic dataset: `python data_generation/generate_synthetic_data.py`
3. Create the MySQL database: run `sql/schema.sql` in MySQL Workbench (or CLI)
4. Copy `sql/db_config_template.py` to `sql/db_config.py` and add your MySQL credentials
5. Load the data: `python sql/load_data_to_mysql.py`
6. Run the SQL analysis: `sql/analysis_queries.sql`
7. Run the notebook: `jupyter notebook notebooks/onboardflow_analysis.ipynb`
8. Open `powerbi/OnboardFlow_Dashboard.pbix` in Power BI Desktop (requires MySQL Connector/NET installed)

*Note: because the data generator uses a fixed random seed, re-running Step 2 reproduces the exact same dataset used throughout this project.*

## Business Analyst Deliverables

This project includes the full documentation suite a BA would produce on a real engagement:
- [Stakeholder Interview Notes](docs/stakeholder_interview_notes.md)
- [Business Requirements Document (BRD)](docs/BRD_OnboardFlow.md)
- [Functional Requirements Document (FRD)](docs/FRD_OnboardFlow.md)
- [User Stories](docs/User_Stories.md)
- [RACI Matrix](docs/RACI_Matrix.md)
- AS-IS and TO-BE Process Flow Diagrams
- [Executive Recommendations Memo](recommendations/Executive_Recommendations_Memo.md)

## Author

Adveidh Krishna

Financial Analyst

[LinkedIn](https://www.linkedin.com/in/akthotarath)
