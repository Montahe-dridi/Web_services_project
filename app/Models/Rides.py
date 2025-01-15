from .db import db

class Ride(db.Model):
    id = db.Column(db.String, primary_key=True)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)