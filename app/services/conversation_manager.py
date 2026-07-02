"""
Purpose:
Analyzes the conversation and decides the next action.

Responsibilities:
- Detect user intent.
- Determine whether clarification is required.
- Detect when the current message answers a previous clarification.
"""

from dataclasses import dataclass


@dataclass
class ConversationState:
    intent: str
    needs_clarification: bool
    clarification_question: str | None = None
    search_query: str | None = None


class ConversationManager:

    def analyze(
        self,
        history: list[dict],
        message: str,
    ) -> ConversationState:

        message = message.strip()

        # --------------------------------------------------
        # CASE 1
        # User is answering a clarification question.
        # --------------------------------------------------

        if history:

            last_message = history[-1]

            if (
                last_message["role"] == "assistant"
                and "job role" in last_message["content"].lower()
            ):

                previous_user = ""

                for item in reversed(history):

                    if item["role"] == "user":

                        previous_user = item["content"]
                        break

                search_query = (
                    previous_user
                    + " "
                    + message
                )

                return ConversationState(
                    intent="recommend",
                    needs_clarification=False,
                    search_query=search_query,
                )

        # --------------------------------------------------
        # CASE 2
        # Comparison request
        # --------------------------------------------------

        if any(
            word in message.lower()
            for word in [
                "compare",
                "difference",
                "vs",
                "versus",
            ]
        ):

            return ConversationState(
                intent="compare",
                needs_clarification=False,
                search_query=message,
            )

        # --------------------------------------------------
        # CASE 3
        # Generic assessment request
        # --------------------------------------------------

        assessment_words = [
            "assessment",
            "test",
            "recommend",
            "hire",
            "hiring",
        ]

        if any(
            word in message.lower()
            for word in assessment_words
        ):

            role_keywords = [
                "developer",
                "engineer",
                "manager",
                "graduate",
                "sales",
                "java",
                "python",
                "analyst",
                "leader",
                "executive",
            ]

            if any(
                role in message.lower()
                for role in role_keywords
            ):

                return ConversationState(
                    intent="recommend",
                    needs_clarification=False,
                    search_query=message,
                )

            return ConversationState(
                intent="recommend",
                needs_clarification=True,
                clarification_question=(
                    "Could you tell me the job role or skills you are hiring for?"
                ),
            )

        # --------------------------------------------------
        # CASE 4
        # Standalone role after no clarification history.
        # --------------------------------------------------

        role_keywords = [
            "developer",
            "engineer",
            "manager",
            "graduate",
            "sales",
            "java",
            "python",
            "analyst",
        ]

        if any(
            role in message.lower()
            for role in role_keywords
        ):

            return ConversationState(
                intent="recommend",
                needs_clarification=False,
                search_query=message,
            )

        # --------------------------------------------------
        # Default
        # --------------------------------------------------

        return ConversationState(
            intent="general",
            needs_clarification=False,
        )