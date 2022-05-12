from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    task = db.Column(db.String(255), unique=False, nullable=False)
    priority = db.Column(db.Integer, unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, user_id, task, priority, done):
        self.user_id = user_id
        self.task = task
        self.priority = priority
        self.done = done