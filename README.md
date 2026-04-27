# GokulAI — Portfolio AI Assistant

A RAG-based AI assistant that answers recruiter and visitor questions about **Gokul Prasath S** in first person. Powered by ChromaDB + OpenAI GPT-4o mini.

---

## What it does

GokulAI is a chatbot embedded in a portfolio site. Ask it anything about Gokul's projects, skills, availability, or background — it answers accurately, in first person, and suggests follow-up questions after every response.

- Answers questions like "What is ClauseGuard?", "What's your salary expectation?", "Are you available for hire?"
- Retrieves the most relevant knowledge chunks before every response (RAG)
- Suggests 2 follow-up questions after each answer
- Offers 6 starter question chips on page load

---

## Architecture

```
User question
     │
     ▼
text-embedding-3-small  ──►  Query vector
                                   │
                                   ▼
                          ChromaDB vector store
                          (165 chunks: Q&A pairs
                           + bio sections + FAQ)
                                   │
                          top-7 relevant chunks
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │  GPT-4o mini             │
                    │  System prompt (persona) │
                    │  + Retrieved context     │
                    │  + Conversation history  │
                    └──────────────────────────┘
                                   │
                                   ▼
                    AssistantResponse
                    { answer, suggested_questions, sources }
                                   │
                                   ▼
                         FastAPI  POST /chat
                                   │
                                   ▼
                    Chat UI  (static/index.html)
```

---

## Setup

```bash
# 1. Create and activate conda environment
conda env create -f environment.yml
conda activate gokulaai

# 2. Add your OpenAI API key
cp .env.example .env
# Edit .env and set: OPENAI_API_KEY=sk-...

# 3. (Optional) Add resume PDF for richer answers
cp /path/to/resume.pdf knowledge/resume.pdf

# 4. Generate synthetic Q&A dataset (~150-200 pairs)
python -m gokulaai.data_generator

# 5. Embed everything and store in ChromaDB
python -m gokulaai.ingestion

# 6. Start the API server
uvicorn gokulaai.api:app --host 0.0.0.0 --port 8000

# 7. Open the chat UI
# http://localhost:8000/static/index.html
```

---

## API Endpoints

| Method | Path       | Description                          |
|--------|------------|--------------------------------------|
| POST   | `/chat`    | Send a message, get an AI response   |
| GET    | `/suggest` | Get 6 starter questions              |
| GET    | `/health`  | Health check                         |

**POST /chat — request body:**
```json
{
  "message": "What is ClauseGuard?",
  "history": [
    { "role": "user",      "content": "..." },
    { "role": "assistant", "content": "..." }
  ]
}
```

**POST /chat — response:**
```json
{
  "answer": "ClauseGuard is a production-grade...",
  "suggested_questions": ["What tech stack?", "How does validation work?"],
  "sources": ["qa_dataset", "master_bio"]
}
```

---

## Updating the knowledge base

All factual content lives in `knowledge/master_bio.md`. To update it:

1. Edit `knowledge/master_bio.md`
2. Regenerate Q&A dataset:
   ```bash
   python -m gokulaai.data_generator
   ```
3. Re-embed and re-ingest:
   ```bash
   python -m gokulaai.ingestion
   ```
4. Restart the server — no code changes needed.

---

## Project structure

```
PersonalAI/
├── gokulaai/
│   ├── api.py              FastAPI app (3 endpoints)
│   ├── assistant.py        GokulAssistant — RAG + chat logic
│   ├── data_generator.py   GPT-4o mini → synthetic Q&A dataset
│   ├── ingestion.py        Embed + store in ChromaDB
│   └── models/schemas.py   Pydantic request/response models
├── knowledge/
│   ├── master_bio.md       Source of truth — edit this to update facts
│   ├── qa_dataset.json     Generated (gitignored — regenerate on setup)
│   └── resume.pdf          Optional — copy your resume here
├── static/
│   ├── index.html          Standalone chat UI
│   └── style.css           Dark theme styles
├── chroma_db/              Local vector store (gitignored)
├── environment.yml         Conda environment definition
└── .env.example            API key template
```

---

## Tech stack

- **LLM:** GPT-4o mini (OpenAI)
- **Embeddings:** text-embedding-3-small (OpenAI)
- **Vector store:** ChromaDB (local, persistent)
- **API:** FastAPI + Uvicorn
- **Data models:** Pydantic v2
- **PDF parsing:** pypdf
- **Token counting:** tiktoken
