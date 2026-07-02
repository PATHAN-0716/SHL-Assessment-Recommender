"""
Purpose:
Tests semantic search on the FAISS vector store.

Run:
    python -m scripts.test_retrieval
"""

from pathlib import Path

from app.embeddings.embedding_model import EmbeddingModel
from app.retriever.vector_store import VectorStore

INDEX_PATH = Path("vector_store")


def main():
    # Load embedding model
    embedding_model = EmbeddingModel()

    # Load FAISS vector store
    vector_store = VectorStore(
        embedding_model.embeddings
    )

    db = vector_store.load(INDEX_PATH)

    # Test query
    query = "Manager communication skills"

    results = db.similarity_search(
        query,
        k=2
    )

    print("=" * 80)
    print(f"Query: {query}")
    print("=" * 80)

    for i, document in enumerate(results, start=1):
        print(f"\nResult {i}")
        print("-" * 80)

        print(document.page_content)

        print("\nMetadata:")
        print(document.metadata)


if __name__ == "__main__":
    main()