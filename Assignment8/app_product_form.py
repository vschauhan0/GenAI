import streamlit as st

name=st.sidebar.text_input("Enter Product name: ")
Color=st.sidebar.selectbox(
    "Select Color: ",
    ["Red","Green","Blue"]
)

if st.sidebar.button("Add Product"):
    st.sidebar.success("Product Added Sucessfully")
    st.sidebar.write(f"Product name: {name}")
    st.sidebar.write(f"Product Color: {Color}")
