# Langchain-python (demo)

A tiny demo showing how to call Google Generative AI via a LangChain wrapper.

This repository is intentionally minimal — the canonical example is `simple_chain.py` and the primary runtime dependency is `langchain_google_genai`.

Quick start

1. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

2. Add your API key to `.env` using the `GOOGLE_API_KEY` variable.

3. Run the demo:

```powershell
python simple_chain.py
```

If the environment variable is missing, `simple_chain.py` will print an error and exit. See `.github/copilot-instructions.md` for agent-focused guidance and development conventions.

Run the FastAPI demo (optional):

```powershell
# start the server locally
uvicorn app:app --reload --port 8000

# health check
curl http://127.0.0.1:8000/health

# generate (PowerShell example) - note: requires GOOGLE_API_KEY in .env
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/generate -Body (@{text='Hello'} | ConvertTo-Json) -ContentType 'application/json'
```

Notes

- `requirements.txt` includes `faiss-cpu`, `fastapi`, and `uvicorn` for future expansion, but there is no server or vectorstore code in this demo yet.
- This repo follows a single-script demo pattern; when adding features, prefer adding small modules and updating the `copilot-instructions` file with any new conventions.

If you want, I can add a minimal `app.py` (FastAPI) example or a short test harness next.
