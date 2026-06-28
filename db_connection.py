import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456789"
    )
    return conn
