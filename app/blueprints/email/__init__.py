from flask import Blueprint


email = Blueprint('email', __name__, template_folder='templates')

from app.blueprints.email import routes