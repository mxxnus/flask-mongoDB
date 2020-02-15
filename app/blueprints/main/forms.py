from app import login,db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import Email, EqualTo, DataRequired

from flask_mongoengine.wtf import model_form

class BillForm(FlaskForm):
    pay_to = StringField('Pay To', validators=[DataRequired()])
    description = StringField('Description')
    amount = IntegerField('Amount',validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    #format='%Y-%m-%d'
    submit = SubmitField('Submit')

    