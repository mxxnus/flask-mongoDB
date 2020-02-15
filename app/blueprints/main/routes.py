from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user
from app.blueprints.main import main

from bson.objectid import ObjectId


@main.route('/', methods=['GET','POST'])
@login_required
def index():
    id = current_user.id
    #test = Bill.objects().order_by('due_date').all()
    print(current_user.id)
    test = Bill.objects(user_id=current_user.id).all()
    
    
    #test = Bill.objects().get(ObjectId(current_user.id))
    
    
    context = {
        #'bills': Bill.objects().order_by('due_date').all()
        'bills': Bill.objects(user=str(current_user.id)).all()   
    }
    return render_template('index.html', **context)