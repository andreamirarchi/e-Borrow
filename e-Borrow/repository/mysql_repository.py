import mysql.connector
from typing import Any, Dict, List, Optional

from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from repositories.base import Repository


class MySqlRepository(Repository):

    def __init__(self):
        self.conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

    def _cursor(self):
        return self.conn.cursor(dictionary=True)

    def load_items(self) -> List[Dict[str, Any]]:
        cursor = self._cursor()
        cursor.execute("SELECT * FROM items")
        return cursor.fetchall()

    def get_item(self, item_id: str) -> Optional[Dict[str, Any]]:
        cursor = self._cursor()
        cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        return cursor.fetchone()

    def add_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        cursor = self._cursor()

        keys = ", ".join(item.keys())
        values = tuple(item.values())
        placeholders = ", ".join(["%s"] * len(item))

        sql = f"INSERT INTO items ({keys}) VALUES ({placeholders})"
        cursor.execute(sql, values)

        self.conn.commit()
        return item