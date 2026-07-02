"""
Purpose:
Builds a structured prompt for Gemini using retrieved SHL assessments.
"""

from langchain_core.documents import Document


class RecommendationPrompt:

    def build(
        self,
        query: str,
        documents: list[Document],
    ) -> str:

        context = []

        for doc in documents:

            meta = doc.metadata

            context.append(
                f"""
Assessment Name: {doc.page_content.splitlines()[1]}

Description:
{doc.page_content}

Duration: {meta.get("duration", "Not Available")}
Remote Testing: {meta.get("remote", "Not Available")}
Adaptive: {meta.get("adaptive", "Not Available")}
Languages: {", ".join(meta.get("languages", [])) or "Not Available"}
URL: {meta.get("url", "Not Available")}
"""
            )

        context = "\n\n----------------------\n".join(context)

        return f"""
You are an SHL Assessment Recommendation Assistant.

Use ONLY the assessments provided below.

Do NOT invent any assessment.

Return your answer in EXACTLY this markdown format.

| Assessment | Remote Testing | Adaptive | Duration | Languages | URL | Why Recommended |
|------------|---------------|----------|----------|-----------|-----|-----------------|

Rules:
- Only recommend the best matching assessments.
- Use the URL provided.
- If any field is missing, write "Not Available".
- After the table, write a short summary (2-3 sentences).

User Requirement:
{query}

Retrieved Assessments:
{context}
"""