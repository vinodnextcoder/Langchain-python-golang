import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Get API key
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

# Set OpenAI-compatible environment variables for OpenRouter
os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

# Create LLM
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    temperature=0.7,
    api_key=OPENROUTER_KEY,
)

# Create agent
agent = create_agent(
    llm,
    tools=[],
    system_prompt="You are a helpful assistant. Answer in simple words."
)

# User input
user_question = "What is artificial intelligence in simple terms?"

# Invoke agent
response = agent.invoke({
    "messages": [
        {"role": "user", "content": user_question}
    ]
})

# Extract and print AI response safely
if "messages" in response and len(response["messages"]) > 0:
    ai_message = response["messages"][-1]
    print(ai_message.content)
else:
    print("No response received from the agent.")
