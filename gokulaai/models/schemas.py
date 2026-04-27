from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = []


class AssistantResponse(BaseModel):
    answer: str
    suggested_questions: list[str] = []
    sources: list[str] = []


class HealthResponse(BaseModel):
    status: str
    model: str
