
"""
Purpose:
Tests whether the DataLoader can successfully load the SHL catalog.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.data.data_loader import DataLoader


catalog_path = ROOT / "data" / "raw" / "shl_product_catalog.json"
loader = DataLoader(catalog_path)

catalog = loader.load()

print(type(catalog))
print(len(catalog))
print(catalog[0])