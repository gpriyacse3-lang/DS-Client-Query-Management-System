import streamlit as st
from datetime import datetime
from db_connection import get_connection

def client_page(username):
    st.header("Client Query Submission")

    email = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        if email and mobile and heading and description:
            conn = get_connection()
            cursor = conn.cursor()

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
                email,
                mobile,
                heading,
                description,
                "Open",
                datetime.now(),
                None
            ))

            conn.commit()
            cursor.close()
            conn.close()

            st.success("Query submitted successfully")
        else:
            st.error("Please fill all fields")
