class BorrowEntity:
    def __init__(self, id, itemName, message):
        self.id = id
        self.itemName = itemName
        self.message = message
        self.status = ""

    def priority(self):
        return 0
