"""
Purpose:
Handles all interactions with Google's Gemini model.

Responsibilities:
- Load API key
- Initialize Gemini client
- Send prompts
- Return generated response
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiService:
    """
    Wrapper around Google's official Gemini SDK.
    """

    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-2.5-flash"

        print("Gemini Client Initialized")

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Sends prompt to Gemini and returns response text.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return response.text

        except Exception as e:

            return f"Gemini Error:\n{str(e)}"