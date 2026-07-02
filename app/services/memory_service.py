"""
Purpose:
Stores conversation history for each chat session.

Responsibilities:
- Save user and assistant messages.
- Return conversation history.
"""

class MemoryService:
    """
    In-memory conversation storage.
    """

    def __init__(self):

        self.sessions = {}

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str,
    ):

        if session_id not in self.sessions:

            self.sessions[session_id] = []

        self.sessions[session_id].append(
            {
                "role": role,
                "content": message,
            }
        )

    def get_history(
        self,
        session_id: str,
    ):

        return self.sessions.get(
            session_id,
            [],
        )