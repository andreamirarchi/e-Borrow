from __future__ import annotations

import sys
from pathlib import Path

from flask import Flask, render_template, request, jsonify, redirect
from flasgger import Swagger

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from forms.borrow_forms import BorrowRequestForm, OfferForm
from schemas.borrow_request_schema import BorrowRequestSchema
from schemas.offer_schema import OfferSchema

from repository_factory import get_repository
from services.borrow_service import BorrowService
from settings import DATABASE_MODE

app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))

app.config["SECRET_KEY"] = "e-borrow_secret"
app.config["WTF_CSRF_ENABLED"] = False

Swagger(app)

repo = get_repository()
service = BorrowService(repo)

print("DATABASE_MODE =", DATABASE_MODE)


@app.route("/")
def home():
    return render_template(
        "home.html",
        request_form=BorrowRequestForm(),
        offer_form=OfferForm(),
        requests=service.get_requests(),
        offers=service.get_offers()
    )


@app.route("/request", methods=["POST"])
def create_request_form():
    form = BorrowRequestForm()

    if form.validate_on_submit():
        service.create_request({
            "itemName": form.itemName.data,
            "message": form.message.data,
            "time": form.time.data,
            "borrower": form.borrower.data
        })
        return redirect("/")

    return "Form non valido", 400


@app.route("/offer", methods=["POST"])
def create_offer_form():
    form = OfferForm()

    if form.validate_on_submit():
        service.create_offer({
            "itemName": form.itemName.data,
            "message": form.message.data,
            "lender": form.lender.data
        })
        return redirect("/")

    return "Form non valido", 400


@app.route("/api/requests", methods=["GET"])
def api_requests():
    return jsonify(service.get_requests())


@app.route("/api/offers", methods=["GET"])
def api_offers():
    return jsonify(service.get_offers())


@app.route("/api/request", methods=["POST"])
def api_create_request():
    schema = BorrowRequestSchema()

    try:
        data = schema.load(request.get_json(force=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    result = service.create_request(data)
    return jsonify(schema.dump(result)), 201


@app.route("/api/offer", methods=["POST"])
def api_create_offer():
    schema = OfferSchema()

    try:
        data = schema.load(request.get_json(force=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    result = service.create_offer(data)
    return jsonify(schema.dump(result)), 201


@app.route("/api/match", methods=["GET"])
def match():
    return jsonify(service.match(
        service.get_offers(),
        service.get_requests()
    ))


@app.route("/api/loan", methods=["POST"])
def create_loan():
    data = request.get_json()

    loan = service.create_loan(
        data["requestId"],
        data["offerId"]
    )

    return jsonify(loan), 201


if __name__ == "__main__":
    print("Avviando l'app...")
    print("Directory:", BASE_DIR)
    print("Tipo repository:", type(repo).__name__)

    #test crud
    print(repo.load_items())
    print(repo.get_item("req_1"))

    app.run(debug=True)