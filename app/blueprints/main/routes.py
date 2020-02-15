from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user
from app.blueprints.main import main

@main.route('/', methods=['GET','POST'])
@login_required
def index():
    id = current_user.id
    #test = Bill.objects(user_id=id).order_by('due_date').all()
    test = Bill.objects().order_by('due_date').all()
    print(test)
    
    context = {
        'bills': Bill.objects().order_by('due_date').all()
        #'bills': Bill.objects(user_id=id)      
    }
    return render_template('index.html', **context)