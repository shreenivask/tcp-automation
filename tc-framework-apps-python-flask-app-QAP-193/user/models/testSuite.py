from models import db
from sqlalchemy import func

class TestSuite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_suite_name = db.Column(db.String(100), unique=True, nullable=False)
    client_id = db.Column(db.Integer, unique=False, nullable=False)
    test_case_ids = db.Column(db.JSON, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    def __repr__(self):
        return f'<User {self.email}>'