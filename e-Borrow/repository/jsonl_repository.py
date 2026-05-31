import json
import os

from repository.base import Repository


class JsonlRepository(Repository):

    def __init__(self, filepath):

        self.filepath = filepath

        if not os.path.exists(filepath):
            open(filepath, "w", encoding="utf-8").close()

    def load_items(self, item_type=None):

        items = []

        with open(
            self.filepath,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                item = json.loads(line)

                if (
                    item_type is None
                    or item.get("type") == item_type
                ):
                    items.append(item)

        return items

    def get_item(self, item_id):

        for item in self.load_items():

            if item.get("id") == item_id:
                return item

        return None

    def add_item(self, item):

        with open(
            self.filepath,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(
                    item,
                    ensure_ascii=False
                )
            )

            f.write("\n")

        return item