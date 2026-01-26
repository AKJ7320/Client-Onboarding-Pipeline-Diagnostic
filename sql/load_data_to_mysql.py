"""
load_data_to_mysql.py
----------------------
Loads the CSVs from data/ into the onboardflow_db MySQL database
(created by sql/schema.sql).

Run this AFTER:
  1. You've run data_generation/generate_synthetic_data.py
  2. You've run sql/schema.sql in MySQL Workbench (or via CLI) to create the database/tables

Run from the PROJECT ROOT:
    python sql/load_data_to_mysql.py

IMPORTANT: Update DB_PASSWORD below with your own MySQL root password
before running (the one you set during MySQL installation).
"""

import pandas as pd
from sqlalchemy import create_engine, URL
from db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
# db_config.py holds your real password and is excluded from Git via .gitignore
# (see db_config_template.py for the format — copy it to db_config.py and fill
# in your real password; db_config.py itself will never be committed).

# Using URL.create() instead of an f-string is deliberate: if your password
# contains special characters like @, #, or :, a plain f-string connection
# string will misparse (the @ gets confused with the host separator).
# URL.create() escapes these safely no matter what's in the password.
connection_url = URL.create(
    "mysql+mysqlconnector",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)
engine = create_engine(connection_url)

# ---------- LOAD ORDER MATTERS ----------
# agents and sla_targets have no foreign keys pointing elsewhere, so they load first.
# applicants references agents (foreign key), so it loads second.
# pipeline_stages and rejections both reference applicants, so they load last.
LOAD_ORDER = [
    ("data/agents.csv", "agents"),
    ("data/sla_targets.csv", "sla_targets"),
    ("data/applicants.csv", "applicants"),
    ("data/pipeline_stages.csv", "pipeline_stages"),
    ("data/rejections.csv", "rejections"),
]

for csv_path, table_name in LOAD_ORDER:
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    print(f"Loaded {len(df):>6} rows into '{table_name}'")

print("\nAll data loaded successfully into onboardflow_db.")
