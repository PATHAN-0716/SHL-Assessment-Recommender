
"""
Purpose:
Tests the complete ChatService.

Run:
    python -m scripts.test_chat_service
"""

from app.services.chat_service import ChatService

service = ChatService()

session = "session_001"

print("=" * 80)
print("USER:")
print("Need assessment")

print("\nASSISTANT:")
print(
    service.chat(
        session,
        "Need assessment"
    )
)

print("=" * 80)
print("USER:")
print("Java Developer")

print("\nASSISTANT:")
print(
    service.chat(
        session,
        "Java Developer"
    )
)