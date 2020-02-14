from flask import render_template
from app import db
from app.models import User

from app.blueprints.main import main

@main.route('/')
def index():
    #u = User(name='derek', email='poo@email.com', password='123456')
    #u.save()
    pass
    return render_template('index.html')