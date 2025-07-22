import streamlit as st

st.title("Home Page")

if(st.button("Go to about section")):
    st.switch_page("pages/1_About.py")