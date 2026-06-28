import streamlit as st
from login import register_user, login_user
from client_page import client_page
from support_page import support_page

def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.success("Logged out successfully")
    st.rerun()

st.set_page_config(page_title="Client Query Management System")


st.title("Client Query Management System")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Register New User")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Select Role", ["Client", "Support"])

    if st.button("Register"):
        register_user(username, password, role)
        st.success("User registered successfully")
        st.info("Go to Login to continue")

elif choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(username, password)

        if result:
            st.session_state.logged_in = True
            st.session_state.role = result[0]
            st.session_state.username = username
            st.success(f"Login successful as {result[0]}")
        else:
            st.error("Invalid username or password")


if st.session_state.logged_in:
    st.sidebar.markdown("---")
    st.sidebar.write(f"👤 User: {st.session_state.username}")
    st.sidebar.write(f"🔐 Role: {st.session_state.role}")

    if st.sidebar.button("Logout"):
        logout()

    if st.session_state.role == "Client":
        client_page(st.session_state.username)
    else:
        support_page()

