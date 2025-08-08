import streamlit as st

@st.dialog("Are you sure?")
def delete_account():
  st.write("")
try:
  if is_logged_in is True:
    pass
except NameError:
  is_logged_in = False
finally:
  if is_logged_in is True:
    st.title("Settings")
    logout = st.button(label="Logout", icon=":material/logout:")
    delete = st.button(label="Delete Account", type="primary", icon=":material/delete_forever:")
    if logout:
      is_logged_in = False
      st.rerun()
    if delete:
      
  elif is_logged_in is False:
    st.title("Please login or sign up")
    login = st.button(label="Login", icon=":material/login:")
    sign_up = st.button(label="Sign Up", icon=":material/add:")
    if login:
      with open("passwords.txt", r) as f:
        pw = st.text_input(label=" ", type="password", label_visibility="collapsed", placeholder="e.g. password#123", icon=":material/password:")
        if pw in f.readlines():
          is_logged_in = True
      st.rerun()
        else:
          st.markdown(":red[This account does not exist]")
    if sign_up:
      with open("passwords.txt", a) as f:
        npw = st.text_input(label=" ", type="password", label_visibility="collapsed", placeholder="e.g. password#123", icon=":material/password:")
        f.write(npw)
      st.rerun()
      
