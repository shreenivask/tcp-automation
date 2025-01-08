from models import db
from sqlalchemy import func

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_case_name = db.Column(db.String(100), unique=True, nullable=False)
    client_id = db.Column(db.Integer, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    test_function = db.Column(db.String(250), unique=False, nullable=False)
    def __repr__(self):
        return f'<User {self.email}>'