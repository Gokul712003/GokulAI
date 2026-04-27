"""Basic smoke tests for GokulAssistant."""
import pytest


def test_import():
    from gokulaai.models.schemas import (
        AssistantResponse,
        ChatMessage,
        ChatRequest,
        HealthResponse,
    )
    assert AssistantResponse
    assert ChatMessage
    assert ChatRequest
    assert HealthResponse


def test_chat_request_defaults():
    from gokulaai.models.schemas import ChatRequest
    req = ChatRequest(message="hello")
    assert req.message == "hello"
    assert req.history == []


def test_assistant_response_defaults():
    from gokulaai.models.schemas import AssistantResponse
    resp = AssistantResponse(answer="test answer")
    assert resp.answer == "test answer"
    assert resp.suggested_questions == []
    assert resp.sources == []
