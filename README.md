## Legal Sathi — AI Legal Advisor for Indian Jurisdiction

An elegant, production‑ready chatbot that answers questions about Indian law using your curated legal PDFs. Built with Flask, LlamaIndex, Google GenAI (Gemini 2.5 Flash), and Hugging Face embeddings, with persistent local vector storage for fast, private retrieval.

### Why this project
- **Accurate, context‑grounded answers**: Responses are constrained to your provided legal documents.
- **Safety‑aware prompting**: Clear safety guidance and disclaimers for sensitive situations.
- **Fast and private**: Local vector store in `./storage`, no external database required.
- **Simple to run**: One‑time indexing, then start the Flask app and chat in your browser.

### Demo (Local)
- Start the app and open `http://localhost:8080`.
- Ask: “What is the process to file an FIR?” or “Explain Section 190 of CrPC.”

---


## Features
- **Retrieval‑Augmented Generation (RAG)** over your legal PDFs in `data/`.
- **Prompting tailored for Indian law** with safety and disclaimer logic (see `src/prompt.py`).
- **Persistent vector index** so you index once and chat instantly next time.
- **Modern UI** with typing indicator and polished styling (see `templates/home.html`).

---

## Prerequisites
- Python 3.10+
- A Google Generative AI API key (for Gemini)
- A Hugging Face access token (for embeddings)

Create a `.env` file at the project root with:

```bash
GOOGLE_API_KEY=your_google_genai_api_key
HF_TOKEN=your_huggingface_access_token
```

Notes:
- Get a Google API key from the Google AI Studio.
- Get a Hugging Face token from your HF profile (Settings → Access Tokens), ensure it has read access to models.

---

## Installation

Clone and install dependencies (Windows PowerShell, macOS, or Linux):

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

pip install --upgrade pip
pip install -r requirements.txt
```

Alternatively, with `uv` (optional):

```bash
uv venv
uv pip install -r requirements.txt
```

---

## Prepare your data
Place your legal PDFs inside the `data/` directory (already includes samples like Constitution, CPC, etc.). You can add or replace PDFs at any time.

---

## One‑time: build the vector index
Run the following to embed documents and persist the index to `./storage`:

```bash
python -c "from src.vector_store import vector_store; vector_store()"
```

If you update files in `data/`, re‑run the same command to refresh the index.

---

## Run the app

```bash
python main.py
```

Then open `http://localhost:8080` in your browser.

Default settings:
- Host: `0.0.0.0`
- Port: `8080`
- Debug: `True` (see `main.py`)

---

## Configuration
- LLM: set in `src/helper.py` (`GoogleGenAI(model="gemini-2.5-flash")`). You can swap to other supported Gemini models.
- Embeddings: set in `src/helper.py` (`BAAI/bge-small-en-v1.5`). You can change to another HF embedding model with good retrieval quality.
- Chunking: `SentenceSplitter(chunk_size=1000, chunk_overlap=150)` in `src/helper.py`.
- Prompt: structured guidance for Indian law and safety handling in `src/prompt.py`.

---

## Project structure

```text
Legal Advisor Chatbot/
├─ data/                       # Your legal PDFs
├─ src/
│  ├─ helper.py                # LLM, embeddings, splitter
│  ├─ vector_store.py          # Index build/load utilities
│  └─ prompt.py                # Domain‑specific system prompt
├─ storage/                    # Persisted vector index (auto‑created)
├─ templates/
│  └─ home.html                # Stylish chat UI
├─ main.py                     # Flask app entrypoint
├─ requirements.txt
├─ pyproject.toml
└─ README.md
```

---

## How it works (high level)
1. Documents in `data/` are split into chunks.
2. Each chunk is embedded using `BAAI/bge-small-en-v1.5` and stored in `./storage`.
3. At query time, LlamaIndex retrieves the most relevant chunks.
4. The Gemini model generates answers constrained by the retrieved legal context and the safety‑aware prompt.

---

## Troubleshooting
- "GOOGLE_API_KEY not set" or LLM errors: ensure `.env` exists with a valid `GOOGLE_API_KEY` and the shell is restarted.
- "HF_TOKEN not set" or embedding download failures: confirm `HF_TOKEN` is valid and has read access.
- Index load errors: if `./storage` does not exist or is outdated, re‑run the indexing step.
- Port already in use: change the port in `main.py` (Flask `app.run(..., port=8080)`).

---

## Security and privacy
- Your PDFs are processed locally and indexed to `./storage`.
- Calls to the LLM provider (Gemini) send the user prompt and retrieved snippets; do not include private data you don’t want shared.

---

## Disclaimer
This project provides general information about Indian laws and jurisprudence only. It does not constitute formal legal advice or establish an attorney‑client relationship. For specific legal matters, consult a qualified legal professional.

---

## License
Choose a license for your project (e.g., MIT, Apache 2.0) and update this section accordingly.


