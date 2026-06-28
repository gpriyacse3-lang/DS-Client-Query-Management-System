import hashlib
from db_connection import get_connection

def register_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

  
    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
    
        cursor.execute("""
            UPDATE users
            SET hashed_password = %s, role = %s
            WHERE username = %s
        """, (hashed_password, role, username))
        action = "updated"
    else:
       
        cursor.execute("""
            INSERT INTO users (username, hashed_password, role)
            VALUES (%s, %s, %s)
        """, (username, hashed_password, role))
        action = "registered"

    conn.commit()
    cursor.close()
    conn.close()
    print(f"User '{username}' {action} successfully.")