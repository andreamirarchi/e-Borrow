from settings import DATABASE_MODE
from repositories.jsonl_repository import JsonlRepository
from repositories.mysql_repository import MySqlRepository


def get_repository():
    if DATABASE_MODE == "mysql":
        return MySqlRepository()

    elif DATABASE_MODE == "jsonl":
        return JsonlRepository("data/items.jsonl")

    else:
        raise ValueError(f"Unsupported DATABASE_MODE: {DATABASE_MODE}")