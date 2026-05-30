from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class BorrowRequestForm(FlaskForm):
    itemName = StringField("Item Name", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    time = IntegerField("Time", validators=[DataRequired(), NumberRange(min=0)])
    borrower = StringField("Borrower", validators=[DataRequired()])


class OfferForm(FlaskForm):
    itemName = StringField("Item Name", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    lender = StringField("Lender", validators=[DataRequired()])