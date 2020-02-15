from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user
from app.blueprints.main.forms import BillForm

from app.blueprints.main import main

@main.route('/', methods=['GET','POST'])
@login_required
def index():
    form = BillForm()
    if form.validate_on_submit():
        b = Bill(pay_to=form.pay_to.data, description=form.description.data, amount=form.amount.data*100, user_id=current_user.id, due_date=form.due_date.data)
        b.save()
        flash("Bill Reminder Created","success")
        return redirect(url_for('main.index'))
    context = {
        'form':form
    }
    return render_template('index.html', **context)