
import json
from pathlib import Path

# This gets the project root regardless of where you run the script from
BASE_DIR = Path(__file__).resolve().parent.parent  # goes up from scripts/ to project root

DATA_PATH = BASE_DIR / "data" / "raw" / "shl_product_catalog.json"

with open(DATA_PATH, "r", encoding="utf-8") as file:
    catalog = json.load(file)

print(type(catalog))
print(len(catalog))
print(catalog[0])