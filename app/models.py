from app import db, login

import mongoengine as me
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user


class User(me.Document, UserMixin):
    name = me.StringField(max_length=60, required=True)
    email = me.StringField(max_length=60, required=True, unique=True)
    password = me.StringField(max_length=180, required=True)
    created_on = me.DateTimeField(default=datetime.utcnow)

    #meta = {'queryset_class':UserQuerySet}

    def generate_password(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f"<User:{self.name} | {self.email}>"


class Bill(me.Document):
    pay_to = me.StringField(max_length=60, required=True)
    description = me.StringField(max_length=60)
    amount = me.IntField(max_length=60, required=True)
    user_id = me.SequenceField(max_length=60, required=True)
    due_date = me.DateTimeField(required=True)
    created_on = me.DateTimeField(default=datetime.utcnow)


@login.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()