from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Bill
from flask_login import login_required, current_user
from app.blueprints.email.forms import ContactForm
from app.blueprints.email.email import send_email

from app.blueprints.email import email


@email.route('/contact', methods=['GET','POST'])
@login_required
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        send_email()
        flash("Bill Reminder emaild","success")
        #return redirect(url_for('email.contact'))
    context = {
        'form':form
    }
    return render_template('contact.html', **context)