from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user

from app.blueprints.main import main

@main.route('/', methods=['GET','POST'])
@login_required
def index():
    context = {      
    }
    return render_template('index.html', **context)