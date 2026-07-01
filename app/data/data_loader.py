"""
Purpose:
Loads the SHL Product Catalog JSON into memory.
This file is only responsible for reading data.
"""


import json
from pathlib import Path
from typing import Any


class DataLoader:
    """
    Loads the SHL product catalog from disk.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self) -> Any:
        """
        Reads the JSON catalog and returns it as Python objects.
        """
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Catalog file not found: {self.file_path}"
            ) from e

        except json.JSONDecodeError as e:
            raise ValueError(
                "Invalid JSON format."
            ) from e