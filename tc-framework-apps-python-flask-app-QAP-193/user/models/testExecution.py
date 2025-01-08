from models import db
from sqlalchemy import func

class TestExecution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_ticket = db.Column(db.String(25), unique=False, nullable=False)
    test_description = db.Column(db.String(255), unique=False, nullable=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    client_id = db.Column(db.Integer, unique=False, nullable=False)
    test_case_id = db.Column(db.Integer, unique=False, nullable=False)
    test_suite_id  = db.Column(db.Integer, unique=False, nullable=True)
    test_report_file = db.Column(db.String(255), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, unique=True, nullable=False, default=func.now())
    def __repr__(self):
        return f'<User {self.email}>'