import getpass
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Test basic connectivity: Google
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7,
        max_tokens=1024,
        timeout=30,
        max_retries=2
    )

    response = llm.invoke("Hello, this is a test message.")
    print("✅ LangChain-Gemini integration working correctly")
    print(f"Response: {response.content}")

except Exception as e:
    print(f"❌ Setup issue detected: {e}")


langsmith_api_key = os.getenv("LANGSMITH_API_KEY")


# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

# if "LANGSMITH_API_KEY" not in os.environ:
#     os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")

# os.environ["LANGSMITH_TRACING"] = "true"
