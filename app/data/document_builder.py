"""
Purpose:
Converts SHL assessment records into LangChain Document objects.
These documents are later embedded and stored in the vector database.
"""

from typing import Any

from langchain_core.documents import Document


class DocumentBuilder:
    """
    Builds LangChain Document objects from SHL catalog records.
    """

    def build(
        self,
        catalog: list[dict[str, Any]]
    ) -> list[Document]:

        documents = []

        for assessment in catalog:

            page_content = f"""
Assessment Name:
{assessment.get("name", "")}

Description:
{assessment.get("description", "")}

Job Levels:
{", ".join(assessment.get("job_levels", []))}

Categories:
{", ".join(assessment.get("keys", []))}
""".strip()

            metadata = {
                "entity_id": assessment.get("entity_id"),
                "name": assessment.get("name"),          # <-- Added
                "url": assessment.get("link"),
                "duration": assessment.get("duration"),
                "remote": assessment.get("remote"),
                "adaptive": assessment.get("adaptive"),
                "languages": assessment.get("languages"),
            }

            documents.append(
                Document(
                    page_content=page_content,
                    metadata=metadata,
                )
            )

        return documents