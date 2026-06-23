import hashlib
from db_connection import get_connection

# convert password to hash
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# register new user
def register_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    cursor.execute("""
        INSERT INTO users (username, hashed_password, role)
        VALUES (%s, %s, %s)
    """, (username, hashed_password, role))

    conn.commit()
    cursor.close()
    conn.close()

# login user
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    cursor.execute("""
        SELECT role FROM users
        WHERE username = %s AND hashed_password = %s
    """, (username, hashed_password))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

