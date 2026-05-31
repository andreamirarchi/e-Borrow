from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class Repository(ABC):

    @abstractmethod
    def load_items(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_item(self, item_id: str) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def add_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        pass