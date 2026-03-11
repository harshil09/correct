import streamlit as st

st.title("Welcome to Universal Banking App")
st.write("Hello Harshil")

name=st.text_input("Enter your name")

if name:
    st.write(f"Welcome {name}")