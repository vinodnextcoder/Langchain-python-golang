import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the key using os.environ or os.getenv()
# os.environ is a dictionary-like object representing the environment variables
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

if GEMINI_API_KEY:
    print("API Key loaded successfully!")
else:
    print("Error: GOOGLE_API_KEY not found in environment or .env file.")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Initialize the model
# Choose a model that supports chat, e.g., 'gemini-2.5-flash'
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=GEMINI_API_KEY)

# Invoke the model with a prompt
response = llm.invoke("Get weather forecast for pune for the next 3 days.")

# Print the response
print(response.content)