from models import db
from sqlalchemy import func

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), unique=True, nullable=False)
    IsActive = db.Column(db.Integer, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    def __repr__(self):
        return f'<User {self.email}>'