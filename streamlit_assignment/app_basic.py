# Task 1 - Basic Streamlit App 

# Import Streamlit Library
import streamlit as st

# Display a Title
st.title("Welcome to Streamlit!")

# Take name text input from user
name = st.text_input("Please Enter your name: ")

# Display a greeting message when the button is clicked
if st.button("Greet Me"):
    st.write(f"Hello, {name}")