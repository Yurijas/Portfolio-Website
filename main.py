from app import app, db
from app.models import Contact, User

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'Contact':Contact, 'User':User } 
