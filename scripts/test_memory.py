"""
Purpose:
Tests MemoryService.

Run:
    python -m scripts.test_memory
"""

from app.services.memory_service import MemoryService

memory = MemoryService()

session = "abc123"

memory.add_message(
    session,
    "user",
    "Need assessment"
)

memory.add_message(
    session,
    "assistant",
    "Which role?"
)

memory.add_message(
    session,
    "user",
    "Java Developer"
)

history = memory.get_history(session)

for message in history:

    print(message)