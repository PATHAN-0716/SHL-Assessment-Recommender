"""
Purpose:
Defines request and response models for the API.
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str
    retrieved_assessments: list[str]
    latency_ms: float