from settings import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=False, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
