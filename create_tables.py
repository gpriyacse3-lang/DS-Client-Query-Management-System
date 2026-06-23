from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);
""")

# queries table
cursor.execute("""
CREATE TABLE IF NOT EXISTS queries (
    query_id SERIAL PRIMARY KEY,
    mail_id VARCHAR(100),
    mobile_number VARCHAR(20),
    query_heading VARCHAR(200),
    query_description TEXT,
    status VARCHAR(20),
    query_created_time TIMESTAMP,
    query_closed_time TIMESTAMP
);
""")

conn.commit()
cursor.close()
conn.close()

print("Tables created successfully")
