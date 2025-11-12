## Purpose

This repository is a small demo that shows how to call Google Generative AI via a LangChain wrapper. These instructions orient AI coding agents to the project's minimal surface so they can make safe, targeted edits.

## Quick start (what humans run locally)

1. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

2. Add your API key to `.env` using the `GOOGLE_API_KEY` variable (the repo includes a placeholder `.env`).

3. Run the demo script:

   ```powershell
   python simple_chain.py
   ```

If the `GOOGLE_API_KEY` is missing, `simple_chain.py` prints an error and exits — treat that as the first debugging step.

## Big picture (in one paragraph)

This repo is a tiny example app: a single script (`simple_chain.py`) that loads an API key from `.env`, instantiates `ChatGoogleGenerativeAI` from `langchain_google_genai`, then calls `llm.invoke(...)` and prints the response. Dependencies in `requirements.txt` suggest the intended expansion path (vector DB via `faiss-cpu`, FastAPI+Uvicorn for a server surface), but those are not yet implemented here.

## Key files and patterns

- `simple_chain.py` — canonical example. Patterns to follow when modifying:
  - Environment: uses `python-dotenv` and `os.getenv('GOOGLE_API_KEY')`.
  - LLM usage: instantiate `ChatGoogleGenerativeAI(model="<model-name>", google_api_key=GEMINI_API_KEY)` and call `invoke()`.
  - Model strings: examples include `gemini-2.5-flash` (used in the demo).

- `requirements.txt` — lists runtime deps. When adding libs, prefer pinning minimally (e.g., `langchain>=0.0`) consistent with the file.

- `.env` — single discoverable env var: `GOOGLE_API_KEY`.

## Project-specific conventions

- Single-script demo style: follow `simple_chain.py` for minimal, imperative examples rather than building new complex modules unless adding features.
- Explicit env-var checks: code prints an error when `GOOGLE_API_KEY` is missing — keep or improve that explicit behaviour (don’t silently fail).

## Integration points & external dependencies

- Google Generative AI via `langchain_google_genai.ChatGoogleGenerativeAI` (pass `google_api_key`).
- `python-dotenv` is used to load `.env` for local development.
- `faiss-cpu` is present in `requirements.txt` but not used; expect future vectorstore work if you add embeddings/recall.

## Concrete examples for common edits

- To add a new model switcher, mimic the existing instantiation:

  ```py
  llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY)
  resp = llm.invoke("Your prompt")
  print(resp.content)
  ```

- To add a FastAPI server later, use `uvicorn` (already in `requirements.txt`) and place the app in a new `app.py`; keep `.env` usage consistent.

## What NOT to change without tests

- Avoid changing the env-var name `GOOGLE_API_KEY` or how `.env` is loaded; the demo and any CI/human instructions expect that key name.

## Verification steps after changes

1. Run `python simple_chain.py` and verify it either prints the API-key-missing message or a valid model response.
2. If you add endpoints, install deps and run `uvicorn app:app --reload` and confirm startup (no server file exists in this repo yet).

---
If anything here looks incomplete or you want deeper coverage (for example, adding tests, expanding to a FastAPI service, or wiring FAISS embeddings), tell me which direction and I will extend these agent instructions.
