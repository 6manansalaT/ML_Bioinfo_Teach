import streamlit as st
import Agent.test_build_agent as test_build_agent
import asyncio


st.title("ML in Bioinformatics Explained")

user_query = st.text_input("🧬 What Machine Learning in Bioinformatics topic would you like to learn about today?", "Enter text here...")

if st.button("Submit"):
    result = asyncio.run(test_build_agent.main(user_query))
    st.success(result)
