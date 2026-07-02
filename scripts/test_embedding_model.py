"""
Purpose:
Tests whether the HuggingFace embedding model loads correctly.

Run:
    python -m scripts.test_embedding_model
"""

from app.embeddings.embedding_model import EmbeddingModel

embedding_model = EmbeddingModel()

model = embedding_model.get_model()

print(type(model))