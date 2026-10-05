import streamlit as st

st.title("feelings developed radar")

gender = st.radio("are you a boy or a girl", ["boy", "girl"])
status = st.selectbox("what do you feel now ?", ["glad", "sad", "cold"])

if st.button("discover yourself !"):
    if status == "glad":
        st.balloons()
        st.success("what a great day !")
    elif status == "sad":
        st.info("don't be sad, tomorrow will be better")
    elif status == "cold":
        st.snow()
