"""
Purpose:
Coordinates the complete SHL recommendation workflow.
"""

from pathlib import Path

from app.embeddings.embedding_model import EmbeddingModel
from app.llm.gemini_service import GeminiService
from app.prompts.recommendation_prompt import RecommendationPrompt
from app.retriever.vector_store import VectorStore
from app.services.conversation_manager import ConversationManager
from app.services.memory_service import MemoryService


class ChatService:

    def __init__(self):

        self.manager = ConversationManager()

        self.memory = MemoryService()

        self.prompt_builder = RecommendationPrompt()

        self.gemini = GeminiService()

        embedding_model = EmbeddingModel()

        self.vector_store = VectorStore(
            embedding_model.embeddings
        )

        self.db = self.vector_store.load(
            Path("vector_store")
        )

    def chat(
        self,
        session_id: str,
        message: str,
    ) -> str:

        history = self.memory.get_history(session_id)

        self.memory.add_message(
            session_id,
            "user",
            message,
        )

        state = self.manager.analyze(
            history,
            message,
        )

        if state.needs_clarification:

            self.memory.add_message(
                session_id,
                "assistant",
                state.clarification_question,
            )

            return state.clarification_question

        query = state.search_query or message

        documents = self.db.similarity_search(
            query,
            k=5,
        )

        prompt = self.prompt_builder.build(
            query,
            documents,
        )

        response = self.gemini.generate(
            prompt,
        )

        self.memory.add_message(
            session_id,
            "assistant",
            response,
        )

        return response