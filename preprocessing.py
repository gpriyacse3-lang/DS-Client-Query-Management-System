import pandas as pd
import re

df = pd.read_csv("queries.csv")

print("Columns in CSV:", df.columns)

if "query_heading" in df.columns and "query_description" in df.columns:
    df.dropna(subset=["query_heading", "query_description"], inplace=True)


if "query_created_time" in df.columns:
    df["query_created_time"] = pd.to_datetime(df["query_created_time"], errors="coerce")
if "query_closed_time" in df.columns:
    df["query_closed_time"] = pd.to_datetime(df["query_closed_time"], errors="coerce")

if "mobile_number" in df.columns:
    df["mobile_number"] = df["mobile_number"].astype(str)


if "status" in df.columns:
    df["status"] = df["status"].str.strip().str.capitalize()


if "query_id" in df.columns:
    df.drop_duplicates(subset=["query_id"], inplace=True)

if "mail_id" in df.columns:
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    df = df[df["mail_id"].apply(lambda x: bool(re.match(email_pattern, str(x))))]

if "mobile_number" in df.columns:
    df = df[df["mobile_number"].apply(lambda x: len(x) == 10 and x.isdigit())]

df.to_csv("queries_cleaned.csv", index=False)
print("✅ Preprocessing complete. Cleaned file saved as queries_cleaned.csv")
print(df.head())
