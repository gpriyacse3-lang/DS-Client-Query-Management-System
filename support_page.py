import streamlit as st
import pandas as pd
from datetime import datetime
from db_connection import get_connection

def support_page():
    st.header("Support Team Dashboard")

    # Filter option
    status_filter = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

    conn = get_connection()

    if status_filter == "All":
        query = "SELECT * FROM queries ORDER BY query_created_time DESC"
    else:
        query = "SELECT * FROM queries WHERE status=%s ORDER BY query_created_time DESC"

    if status_filter == "All":
        df = pd.read_sql(query, conn)
    else:
        df = pd.read_sql(query, conn, params=(status_filter,))

    st.subheader("All Queries")
    st.dataframe(df)

    st.subheader("Close a Query")

    query_id = st.number_input("Enter Query ID to Close", step=1)

    if st.button("Close Query"):
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE queries
            SET status=%s, query_closed_time=%s
            WHERE query_id=%s
        """, ("Closed", datetime.now(), query_id))

        conn.commit()
        cursor.close()
        st.success("Query closed successfully")

    conn.close()
