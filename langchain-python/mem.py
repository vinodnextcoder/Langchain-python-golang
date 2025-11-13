import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


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
agent = create_agent(llm,
                     tools=[get_weather],
                     system_prompt="You are a helpful assistant")
# Run the agent
test =  agent.invoke(
    {"messages": [{"role": "user", "content": "What's lion"}]}
)
print(test) 
