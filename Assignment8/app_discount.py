import streamlit as st

Price=st.number_input("Original Price: ")
Discount=st.slider("Selct Discount: ", 0, 50, 1)
final_price=Price-Price*Discount/100

if st.button("Calculate"):
    st.success(f"Final price: {final_price}")

Data={
    "Before":[Price],
    "After":[final_price]
}

st.table(Data)