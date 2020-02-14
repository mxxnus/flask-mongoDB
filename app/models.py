from app import db, login

import mongoengine as me
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Document):
    name = me.StringField(max_length=60, required=True)
    email = me.StringField(max_length=60, required=True, unique=True)
    password = me.StringField(max_length=180, required=True)
    created_on = me.DateTimeField(default=datetime.utcnow)


    def generate_password(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password,password)

@login.user_loader
def get_user(id):
    return User.query.get(int(id))