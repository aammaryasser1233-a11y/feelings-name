

import streamlit as st
st.title("feelings developed radar")
gender = st.radio("are you a boy or a girl"("boy"),("girl")")
status = st.selectbox("what do you feel now ?("glad","sad","cold")")
if st.bottun("descover yourself !"):
  if status == "glad":
    st.fireworks()
    st.success("what a greet day !")

  elif status == "sad":
  st.info("donnot be sad , tommorw will be better")

  elif status =="cold":
    st.snow()
