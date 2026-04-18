import getpass
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")


# Initialize the LLM instance for export
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    google_api_key=api_key,
    temperature=0.7,
    max_tokens=4096,
    timeout=30,
    max_retries=2
)

# Test basic connectivity only when running this script directly
if __name__ == "__main__":
    try:
        response = llm.invoke("Hello, this is a test message.")
        print("✅ LangChain-Gemini integration working correctly")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"❌ Setup issue detected: {e}")

langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
if langsmith_api_key:
    os.environ["LANGSMITH_API_KEY"] = langsmith_api_key
    os.environ["LANGSMITH_TRACING"] = "true"
    print("📡 LangSmith tracing enabled")