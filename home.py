from settings import is_logged_in

import streamlit as st

def home(is_logged_in):
    if is_logged_in is True:
        st.title("Home")
        st.write("Welcome to your account.")
    elif is_logged_in is False:
        st.title("Please login in the settings tab first.")

pages = [
    st.Page(page=home(is_logged_in), title="Home", icon=":material/home:"),
    st.Page(page="settings.py", title="Settings", icon=":material/settings:")
]
pgs = st.navigation(pages)
pgs.run()
