"""
Purpose:
Tests the ConversationManager.

Run:
    python -m scripts.test_conversation_manager
"""

from app.services.conversation_manager import ConversationManager

manager = ConversationManager()

queries = [
    "Need assessment",
    "Need Java developer assessment",
    "Compare OPQ and MTA",
    "Hello"
]

for query in queries:

    state = manager.analyze(query)

    print("=" * 60)
    print(query)
    print(state)