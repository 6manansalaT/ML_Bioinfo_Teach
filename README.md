# ML in Bioinformatics Explained:

This app explains a plethora Machine Learning
in Bioinformatics topics with the use of a Gemini LLM. It serves as a credible source for 
educational information via a MCP server and a simple user web-interface. 

**Tools:**
- Google Gemini API 3.1 Flash AI model
- PubMed MCP Server
- Streamlit GUI


### Installation + Setup Requirements:
1. Set up virtual environment for best results
~~~
python -m venv langchain-gemini-env
~~~
 
Linux/Mac: 
```source langchain-gemini-env/bin/activate```
 
Windows: 
```langchain-gemini-env\Scripts\activate```

2. Install packages required for Langchain-Gemini-MCP integration
~~~
pip install langchain>=0.1.0
pip install langchain-google-genai
pip install python-dotenv
pip install langchain-community
pip install langchain-mcp-adapters
~~~

3. Install packages for Rich & Streamlit
~~~~
pip install streamlit
pip install streamlit-keypress
pip install rich
~~~

4. Inside virtual environment, run Streamlit app
~~~
streamlit run streamlit_app.py
~~~

5. Enter any topic to learn about its ML concepts and recent applications in research.