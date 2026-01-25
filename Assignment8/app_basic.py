import streamlit as st

st.title("Welcome to Streamlit !")
st.text_input("Enter Your name: ")

if st.button("Great me!"):
    st.write('"Hello, !"')