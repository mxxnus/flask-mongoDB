import os
from flask import Flask
from flask_mongoengine import MongoEngine

from config import Config

from flask_login import LoginManager
login = LoginManager()
login.login_view = 'account.login'
login.login_message_category = 'danger'

db = MongoEngine()

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    #app.config['MONGODB_SETTINGS'] = {
        #"db": "bills"
    #}


    db.init_app(app)

    login.init_app(app)


    from app.blueprints.main import main
    app.register_blueprint(main, url_prefix='/')
        
    from app.blueprints.account import account
    app.register_blueprint(account, url_prefix='/account')

    from app.blueprints.bill import bill
    app.register_blueprint(bill, url_prefix='/bill')

    with app.app_context():
        from app import models
    return app



