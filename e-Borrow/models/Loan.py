from models.BorrowEntity import BorrowEntity


class Loan(BorrowEntity):
    def __init__(self, id, itemName, message, borrower, lender):
        super().__init__(id, itemName, message)
        self.borrower = borrower
        self.lender = lender
        self.status = "preso in carico"
