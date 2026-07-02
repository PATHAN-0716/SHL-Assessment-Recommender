"""
Purpose:
Defines chat API endpoints.
"""

from fastapi import APIRouter

from app.models.schemas import (
    ChatRequest,
    ChatResponse,
)
from app.services.chat_service import ChatService

router = APIRouter()

service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):

    answer = service.chat(
        request.session_id,
        request.message,
    )

    return ChatResponse(
        response=answer,
    )

@router.get("/health")
def health():

    return {
        "status": "healthy"
    }