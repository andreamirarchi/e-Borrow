from config.settings import DATABASE_MODE


def get_repository():

    if DATABASE_MODE == "mysql":

        from repository.mysql_repository import MySqlRepository
        return MySqlRepository()

    elif DATABASE_MODE == "jsonl":

        from repository.jsonl_repository import JsonlRepository
        return JsonlRepository("data/data.jsonl")

    else:
        raise ValueError(
            f"Unsupported DATABASE_MODE: {DATABASE_MODE}"
        )