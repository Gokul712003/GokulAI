"""
FastAPI application for GokulAI.
"""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from gokulaai.assistant import GokulAssistant
from gokulaai.models.schemas import AssistantResponse, ChatRequest, HealthResponse

STATIC_DIR = Path(__file__).parent.parent / "static"

STARTER_QUESTIONS = [
    "What projects have you built?",
    "Tell me about ClauseGuard",
    "What's your technical stack?",
    "Are you available for hire?",
    "What makes you different from other AI/ML freshers?",
    "Tell me about PulseIQ",
]

assistant: GokulAssistant | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global assistant
    assistant = GokulAssistant()
    yield


app = FastAPI(title="GokulAI", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok", model="gpt-4o-mini")


@app.get("/suggest", response_model=list[str])
async def suggest():
    return STARTER_QUESTIONS


@app.post("/chat", response_model=AssistantResponse)
async def chat(request: ChatRequest):
    if assistant is None:
        raise HTTPException(status_code=503, detail="Assistant not ready")
    return assistant.chat(request.message, request.history)


# Mount static files last so API routes take precedence
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
