from models.BorrowRequest import BorrowRequest
from models.Offer import Offer
from models.Loan import Loan

class BorrowService:
    def __init__(self, repo):
        self.repo = repo

    def create_request(self, data):
        req = BorrowRequest(
            id=f"req_{len(self.repo.load_items('request')) + 1}",
            itemName=data["itemName"],
            message=data["message"],
            urgency=data.get("urgency", 0),
            importance=data.get("importance", 0),
            time=data["time"],
            borrower=data["borrower"]
        )

        self.repo.add_item(req.__dict__)
        return req

    def create_offer(self, data):
        offer = Offer(
            id=f"off_{len(self.repo.load_items('offer')) + 1}",
            itemName=data["itemName"],
            message=data["message"],
            lender=data["lender"]
        )

        obj = offer.__dict__
        obj["type"] = "offer"
        obj["status"] = "available"

        self.repo.add_item(obj)
        return offer

    def get_requests(self):
        return self.repo.load_items("request")

    def get_offers(self):
        return self.repo.load_items("offer")

    def create_loan(self, request, offer):
        loan = Loan(
            id=f"loan_{len(self.repo.load_items('loan')) + 1}",
            itemName=request["itemName"],
            message=request["message"],
            borrower=request["borrower"],
            lender=offer["lender"]
        )

        request["status"] = "taken"
        offer["status"] = "taken"
        loan.status = "taken"

        self.repo.add_item(loan.__dict__)

        return loan