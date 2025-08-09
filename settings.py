import streamlit as st

@st.dialog(title="Are you sure?", dismissible=False)
def delete_account():
  st.write("By selecting Yes, your account will be permanently deleted.")
  col1, col2 = st.columns(2)
  no = col1.button(label="No", icon=":material/close:")
  yes = col2.button(label="Yes, and I understand the consequences.", type="primary", icon=":material/delete_forever:")
  if no:
    st.rerun()
  if yes:
    global p
    p = st.text_input(label=" ", type="password", label_visibility="collapsed", placeholder="e.g. password#123", icon=":material/password:")
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
      delete_account()
      with open("passwords.txt", r) as f:
        try:
          if p not in f.readlines:
            pass
        except NameError:
          
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
      
