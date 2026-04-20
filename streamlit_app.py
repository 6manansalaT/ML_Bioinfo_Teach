import streamlit as st
from streamlit_keypress import key_press_events
import Agent.test_build_agent as test_build_agent
import asyncio


st.title("ML in Bioinformatics Explained")

user_query = st.text_input("🧬 What Machine Learning in Bioinformatics topic would you like to learn about today?")

key = key_press_events()

if st.button("Submit"):
    with st.spinner("Agent is working on it..."):
        result = asyncio.run(test_build_agent.main(user_query))
        # st.success(result)
        st.success("Analysis Complete!")
        # st.code(result, language="markdown") # This keeps your sequences perfectly aligned
        st.markdown(result)


if key == 'Enter':
    with st.spinner("Agent is working on it..."):
        result = asyncio.run(test_build_agent.main(user_query))
        # st.success(result)
        st.success("Analysis Complete!")
        # st.code(result, language="markdown") # This keeps your sequences perfectly aligned
        st.markdown(result)
