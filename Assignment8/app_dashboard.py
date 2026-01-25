import streamlit as st

st.title("Simple Sales Dashboard")
st.write("This is a simple sales dashboard which shows sales data month wise")

sales={
    "January":1200,
    "Febuary":1500,
    "March":900,
    "April":2000
}

month=st.selectbox(
    "Select Month",
    ["January","Febuary","March","April"]
)

st.write(f"Sales of {month} is {sales[f'{month}']}")

st.bar_chart(list(sales.values()))