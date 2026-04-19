import streamlit as st
import Agent.test_build_agent as test_build_agent

st.title("Bioinfo MLearning")

user_query = st.text_input("🧬 What ML Bioinformatics topic would you like to learn about today?", "Enter text here...")

if st.button("Submit"):
    result = test_build_agent.build_agent(user_query)
    st.success(result)
