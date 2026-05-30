from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Dict, List, Optional


class JsonlRepository:
    def __init__(self, file_path: str | Path):
        self.file = Path(file_path)
        self.lock = threading.Lock()
        self.file.parent.mkdir(parents=True, exist_ok=True)
        if not self.file.exists():
            self.file.write_text("", encoding="utf-8")

    def load_items(self, item_type: Optional[str] = None) -> List[Dict[str, Any]]:
        items: List[Dict[str, Any]] = []
        try:
            with self.file.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        item = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(item, dict):
                        if item_type is None or item.get("type") == item_type:
                            items.append(item)
        except FileNotFoundError:
            return []
        return items

    # Backward-compatible aliases
    def loadItems(self):
        return self.load_items()

    def getItems(self):
        return self.load_items()

    def getItem(self, id):
        for item in self.load_items():
            if item.get("id") == id:
                return item
        return None

    def add_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        with self.lock:
            with self.file.open("a", encoding="utf-8") as f:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        return item

    def addItem(self, item):
        return self.add_item(item)
