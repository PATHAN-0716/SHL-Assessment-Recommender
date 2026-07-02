"""
Purpose:
Builds, saves, and loads the FAISS vector database.
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:
    """
    Manages the FAISS vector database.
    """

    def __init__(
        self,
        embeddings: HuggingFaceEmbeddings,
    ):
        self.embeddings = embeddings

    def build(
        self,
        documents: list[Document],
    ) -> FAISS:

        return FAISS.from_documents(
            documents,
            self.embeddings,
        )

    def save(
        self,
        vector_store: FAISS,
        path: Path,
    ):

        vector_store.save_local(str(path))

    def load(
        self,
        path: Path,
    ) -> FAISS:

        return FAISS.load_local(
            str(path),
            self.embeddings,
            allow_dangerous_deserialization=True,
        )