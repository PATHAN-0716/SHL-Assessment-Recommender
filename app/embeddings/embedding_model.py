"""
Purpose:
Creates the HuggingFace embedding model used throughout the application.
"""

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Creates a reusable HuggingFace embedding model.
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )