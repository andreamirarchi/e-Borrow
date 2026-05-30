from models.BorrowEntity import BorrowEntity
from utils.priority import offer_priority


class Offer(BorrowEntity):
    def __init__(self, id, itemName, message, lender):
        super().__init__(id, itemName, message)
        self.lender = lender
        self.status = "disponibile"

    def priority(self, requests):
        return offer_priority(self.itemName, requests)
