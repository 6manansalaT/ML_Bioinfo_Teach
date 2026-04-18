from model import llm

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a technical writing assistant specializing in API documentation."),
    HumanMessage(content="Explain the difference between REST and GraphQL APIs in simple terms.")
]

# Generate a response
response = llm.invoke(messages)
print(f"Response: {response.content}")
