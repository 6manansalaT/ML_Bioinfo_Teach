import streamlit as st
st.title("Bioinfo MLearning")

user_query = st.text_input("What do you want to learn today?", "Enter your question...")

if st.button("Submit"):
    result = "Success!"
    st.success(result)