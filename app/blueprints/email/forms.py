from app import login,db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Email, EqualTo, DataRequired

from flask_mongoengine.wtf import model_form

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField(label='Submit')
