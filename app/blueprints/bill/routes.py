from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user
from app.blueprints.bill.forms import BillForm

from app.blueprints.bill import bill

@bill.route('/create', methods=['GET','POST'])
@login_required
def create():
    form = BillForm()
    if form.validate_on_submit():
        b = Bill(pay_to=form.pay_to.data, description=form.description.data, amount=form.amount.data*100, user=str(current_user.id), due_date=form.due_date.data)
        b.save()
        flash("Bill Reminder Created","success")
        return redirect(url_for('main.index'))
    context = {
        'form':form
    }
    return render_template('create.html', **context)


@bill.route('/reminders', methods=['GET','POST'])
@login_required
def reminders():
    context = {
        'bills': Bill.objects(user=str(current_user.id)).all()   
    }
    return render_template('reminders.html', **context)


@bill.route('/delete/<id>')
@login_required
def delete_post(id):

    p = Bill.objects.with_id(id)
    p.delete()

    flash("Post deleted successfully","info")
    return redirect(url_for('bill.reminders'))