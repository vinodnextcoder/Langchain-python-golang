import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import requests

# Load environment variables
load_dotenv()

# Get API key
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

# Set OpenAI-compatible environment variables for OpenRouter
os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

@tool('get_weather', description='Return weather info for city', return_direct=False)
def get_weather(city: str) -> str:
    print(f"Fetching weather for city: {city}")
    """Get current weather for a city using wttr.in API."""
    try:
        # wttr.in supports simple JSON responses
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Extract current condition
        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        wind_kph = current["windspeedKmph"]
        weather_desc = current["weatherDesc"][0]["value"]

        return f"Weather in {city}: {temp_c}°C, Wind: {wind_kph} km/h, Condition: {weather_desc}"

    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"
    except KeyError:
        return "Unexpected response from weather API."
    except Exception as e:
        return f"Error fetching weather: {e}"


# Create LLM
llm = ChatOpenAI(
    model="x-ai/grok-4.1-fast:free",
    temperature=0.7,
    api_key=OPENROUTER_KEY,
)

# Create agent
agent = create_agent(
    llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant weather assistant"
)

# User input


# Invoke agent
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the weather in Mumbai?"}
    ]
})

# Extract and print AI response safely
if "messages" in response and len(response["messages"]) > 0:
    ai_message = response["messages"][-1]
    print(ai_message.content)
else:
    print("No response received from the agent.")
