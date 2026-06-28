import pandas as pd
from db_connection import get_connection
import logging

logging.basicConfig(level=logging.INFO)

# Load CSV
df = pd.read_csv("queries_cleaned.csv")

# Clean dates
df["date_raised"] = pd.to_datetime(df["date_raised"], errors="coerce")
df["date_closed"] = pd.to_datetime(df["date_closed"], errors="coerce")

# Normalize status
df["status"] = df["status"].str.strip().str.capitalize()
df["status"] = df["status"].replace({"Opened": "Open", "Closed": "Closed"})

# Drop rows missing essential fields
df = df.dropna(subset=["client_email", "query_heading", "query_description"])

conn = get_connection()
cursor = conn.cursor()

insert_query = """
    INSERT INTO queries (
        mail_id,
        mobile_number,
        query_heading,
        query_description,
        status,
        query_created_time,
        query_closed_time
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

data = []
for _, row in df.iterrows():
    data.append((
        row["client_email"],
        str(row["client_mobile"]),  # ensure string type
        row["query_heading"],
        row["query_description"],
        row["status"],
        row["date_raised"].to_pydatetime() if pd.notna(row["date_raised"]) else None,
        row["date_closed"].to_pydatetime() if pd.notna(row["date_closed"]) else None
    ))

try:
    cursor.executemany(insert_query, data)
    conn.commit()
    logging.info(f"{len(data)} rows inserted successfully")
except Exception as e:
    conn.rollback()
    logging.error(f"Error inserting data: {e}")
finally:
    cursor.close()
    conn.close()