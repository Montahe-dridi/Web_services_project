from .db import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)