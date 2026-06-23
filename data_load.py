import pandas as pd
from db_connection import get_connection

# Read CSV
df = pd.read_csv("synthetic_client_queries.csv")

# Convert date columns to datetime (very important)
df["date_raised"] = pd.to_datetime(df["date_raised"], errors="coerce")
df["date_closed"] = pd.to_datetime(df["date_closed"], errors="coerce")

conn = get_connection()
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
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
    """, (
        row["client_email"],
        row["client_mobile"],
        row["query_heading"],
        row["query_description"],
        row["status"],
        row["date_raised"].to_pydatetime() if pd.notna(row["date_raised"]) else None,
        row["date_closed"].to_pydatetime() if pd.notna(row["date_closed"]) else None
    ))

conn.commit()
cursor.close()
conn.close()

print("CSV data inserted successfully")
