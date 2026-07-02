"""
Purpose:
Defines request and response models for the API.
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Incoming request body.
    """

    session_id: str
    message: str


class ChatResponse(BaseModel):
    """
    Outgoing response body.
    """

    response: str