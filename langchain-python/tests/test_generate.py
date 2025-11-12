import sys
from types import ModuleType
from fastapi.testclient import TestClient


def test_generate_with_mocked_llm(monkeypatch):
    """Ensure `/generate` returns the LLM content when the LLM is mocked.

    Strategy:
    - Inject a fake `langchain_google_genai` module into sys.modules with a
      `ChatGoogleGenerativeAI` class that returns a predictable response.
    - Set `app.GEMINI_API_KEY` so the endpoint doesn't raise a missing-key error.
    """

    # Create a fake module with a ChatGoogleGenerativeAI class
    fake_mod = ModuleType("langchain_google_genai")

    class FakeLLM:
        def __init__(self, model=None, google_api_key=None):
            self.model = model
            self.google_api_key = google_api_key

        def invoke(self, prompt_text):
            class R:
                pass

            r = R()
            r.content = f"fake response for: {prompt_text}"
            return r

    fake_mod.ChatGoogleGenerativeAI = FakeLLM

    # Inject the fake module so `from langchain_google_genai import ChatGoogleGenerativeAI`
    # inside `app.generate` will pick up the fake implementation.
    sys.modules["langchain_google_genai"] = fake_mod

    # Import app after we patch sys.modules to ensure lazy import inside handler works
    import app

    # Ensure the app thinks there is an API key (app.GEMINI_API_KEY is evaluated at import)
    app.GEMINI_API_KEY = "fake-key"

    client = TestClient(app.app)

    resp = client.post("/generate", json={"text": "hello world"})
    assert resp.status_code == 200
    assert resp.json() == {"content": "fake response for: hello world"}
