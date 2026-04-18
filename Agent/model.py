import getpass
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

# if "LANGSMITH_API_KEY" not in os.environ:
#     os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")

# os.environ["LANGSMITH_TRACING"] = "true"



model = ChatGoogleGenerativeAI(
    model="gemini-3.1-pro-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)