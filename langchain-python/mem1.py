import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
# import langchain_community.agents from Ch
# from langchain_community.chat_models import ChatOpenAI
load_dotenv()
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
utl = "http://localhost:3005/v1"

llm = ChatOpenAI(
    model="phi-3-mini-4k-instruct",
    base_url=utl,
    temperature=0.7,
    api_key=OPENROUTER_KEY,
)
agent = create_agent(llm,
                     tools=[get_weather],
                     system_prompt="You are a helpful assistant")
# Run the agent
test =  agent.invoke(
    {"messages": [{"role": "user", "content": "What is love"}]}
)
print(test) 
