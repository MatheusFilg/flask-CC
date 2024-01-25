from app import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)
    subject = db.Column(db.String, nullable=True)
    contacted_at = db.Column(db.DateTime, default=datetime.now())