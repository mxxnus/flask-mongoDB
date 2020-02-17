from app import create_app, db
from app.models import User, Bill

app = create_app()

@app.shell_context_processor
def get_context():
    return dict(User = User, Bill=Bill, app=app, db=db)