import os
from dotenv import load_dotenv

class Config:  
    MONGODB_SETTINGS={
        "db":"bills"
    }
    SECRET_KEY = os.environ.get('SECRET_KEY')


