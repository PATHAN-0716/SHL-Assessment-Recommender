"""
Purpose:
Coordinates the complete SHL recommendation workflow.
"""

import time
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

        # Lazy-loaded components
        self.gemini = None
        self.vector_store = None
        self.db = None

    def _load_models(self):

        if self.gemini is None:
            self.gemini = GeminiService()

        if self.db is None:

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
    ):

        start = time.perf_counter()

        # Load heavy objects only on first chat request
        self._load_models()

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

            latency = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            return {
                "response": state.clarification_question,
                "retrieved_assessments": [],
                "latency_ms": latency,
            }

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

        latency = round(
            (time.perf_counter() - start) * 1000,
            2,
        )

        retrieved = [
            doc.metadata.get("name", "")
            for doc in documents
        ]

        return {
            "response": response,
            "retrieved_assessments": retrieved,
            "latency_ms": latency,
        }