from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

# Song
class Song(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    minutes = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    interpeter = db.Column(db.String(128))


# Album 
class Medium(Enum):
    DISK = 1
    CASSETTE = 2
    CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    year = db.Column(db.Integer)
    description = db.Column(db.String(255))
    medium = db.Column(db.Integer)

# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    password = db.Column(db.String(32))

