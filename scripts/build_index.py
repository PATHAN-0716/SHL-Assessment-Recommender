"""
Purpose:
Creates the FAISS vector index from the SHL catalog.

Run:
    python -m scripts.build_index
"""

from pathlib import Path

from app.data.data_loader import DataLoader
from app.data.document_builder import DocumentBuilder
from app.embeddings.embedding_model import EmbeddingModel
from app.retriever.vector_store import VectorStore


DATA_PATH = Path("data/raw/shl_product_catalog.json")
INDEX_PATH = Path("vector_store")


loader = DataLoader(DATA_PATH)
catalog = loader.load()

builder = DocumentBuilder()
documents = builder.build(catalog)

embedding_model = EmbeddingModel()

vector_store = VectorStore(
    embedding_model.embeddings
)

index = vector_store.build(documents)

vector_store.save(
    index,
    INDEX_PATH,
)

print("===================================")
print("FAISS index created successfully!")
print(f"Documents indexed : {len(documents)}")
print(f"Saved to          : {INDEX_PATH}")
print("===================================")