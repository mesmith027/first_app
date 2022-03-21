import streamlit as st

st.title("Creating my first Streamlit app")

st.write("helllooo world!!! :smile:")

click = st.button("Press me")

if click:
    st.balloons()

check = st.checkbox("Checkbox here")

if check:
    st.snow()

option = ["Name","Telephone","Address","Email"]

pick = st.selectbox("Choose an option", option)

pick

value = st.slider("My first slider", 150,500)
value
