from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from typing import Dict

load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

app = FastAPI(title="Langchain Python Demo")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate")
def generate(payload: Dict[str, str]):
    """Generate content from the given prompt text.

    Body: {"text": "your prompt here"}
    """
    if not GEMINI_API_KEY:
        # fail fast with a clear message when API key is missing
        raise HTTPException(status_code=400, detail="GOOGLE_API_KEY not set")

    # Import inside the handler to avoid import-time failures when deps are missing
    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY)
    prompt_text = payload.get("text", "")
    resp = llm.invoke(prompt_text)
    return {"content": resp.content}
