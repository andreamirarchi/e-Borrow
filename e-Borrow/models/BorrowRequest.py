from models.BorrowEntity import BorrowEntity
from utils.priority import request_priority


class BorrowRequest(BorrowEntity):
    def __init__(self, id, itemName, message, urgency, importance, time, borrower):
        super().__init__(id, itemName, message)
        self.urgency = urgency
        self.importance = importance
        self.time = time
        self.borrower = borrower
        self.status = "pending"

    def priority(self):
        return request_priority(self.message, self.time)
