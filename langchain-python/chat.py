import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
    api_key=OPENROUTER_KEY,
)

response = llm.invoke("Get weather forecast for Pune for the next 3 days.")
print(response.content)
