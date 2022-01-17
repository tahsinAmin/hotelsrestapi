from flask_sqlalchemy import SQLAlchemy

from src import hotels

db = SQLAlchemy()

class User(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(80), unique=True, nullable=False)
    password   = db.Column(db.Text(), nullable=False)

    def __repr__(self) -> str:
        return 'User>>> {self.username}'


class Hotel(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    title      = db.Column(db.String(), nullable=False)
    price      = db.Column(db.Integer(), nullable=False)
    review     = db.Column(db.String(), nullable=False)
    location   = db.Column(db.String())
    amenities  = db.Column(db.String(), nullable=False)
    image_link = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return 'Hotel>>> {self.title}'