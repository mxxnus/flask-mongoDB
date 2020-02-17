import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.blueprints.email.forms import ContactForm
from flask import render_template

def send_email():
    form = ContactForm()
    context ={
        'recipient_name': 'Derek Moon',
        'sender_name': form.name.data,
        'message': form.message.data,
        'sender_email':form.email.data,
    }

    message = Mail(
        from_email='noreply@mxxnus.com',
        to_emails='lxnkzr@gmail.com',
        subject='Contact Form Inquery',
        html_content=render_template('email.html', **context)
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        
    except Exception as e:
        print(e.message)