"""
Purpose:
Tests the DocumentBuilder by converting the SHL catalog into LangChain Documents.

Run:
    python -m scripts.test_document_builder
"""

from pathlib import Path

from app.data.data_loader import DataLoader
from app.data.document_builder import DocumentBuilder

loader = DataLoader(
    Path("data/raw/shl_product_catalog.json")
)

catalog = loader.load()

builder = DocumentBuilder()

documents = builder.build(catalog)

print(type(documents))
print(len(documents))
print()

print(documents[0].page_content)
print()

print(documents[0].metadata)