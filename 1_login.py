import streamlit as st
import datetime
import pandas as pd
import streamlit as st


def login():
    """Login page"""
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Perform dummy login logic here
        if username == "dummyuser" and password == "dummypassword":
            st.success("Logged in!")
            # Redirect to another page upon successful login
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def home():
    """Home page"""
    st.title("Home")
    st.write("Welcome to the home page!")

# Main Streamlit app
def main():
   
    page = st.sidebar.radio("Navigation", ["Login", "Home"])
    if page == "Login":
        login()
    elif page == "Home":
        home()

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/Jjfa6PH31VRgA/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


if __name__ == "__main__":
    main()
