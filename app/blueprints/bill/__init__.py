from flask import Blueprint


bill = Blueprint('bill', __name__, template_folder='templates')

from app.blueprints.bill import routes