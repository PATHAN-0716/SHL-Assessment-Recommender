"""
Purpose:
Tests the recommendation prompt.

Run:
    python -m scripts.test_prompt
"""

from pathlib import Path

from app.data.data_loader import DataLoader
from app.data.document_builder import DocumentBuilder
from app.embeddings.embedding_model import EmbeddingModel
from app.prompts.recommendation_prompt import RecommendationPrompt
from app.retriever.vector_store import VectorStore

loader = DataLoader(
    Path("data/raw/shl_product_catalog.json")
)

catalog = loader.load()

builder = DocumentBuilder()

documents = builder.build(catalog)

embedding_model = EmbeddingModel()

vector_store = VectorStore(
    embedding_model.embeddings
)

db = vector_store.load(
    Path("vector_store")
)

query = "Java developer assessment"

results = db.similarity_search(
    query,
    k=3,
)

prompt = RecommendationPrompt().build(
    query,
    results,
)

print(prompt)