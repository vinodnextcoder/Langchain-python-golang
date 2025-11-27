import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

# Set OpenAI-compatible environment variables for OpenRouter
os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

# Create LLM model
model = init_chat_model(
    model="x-ai/grok-4.1-fast:free",
    model_provider="openai",
    api_key=OPENROUTER_KEY,
    temperature=0.7
)

# Invoke model
response = model.invoke("What is artificial intelligence in simple terms?")

# Print AI response
print(response.content)
