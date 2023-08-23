from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

# Table for relationship for albums and songs
albums_songs = db.Table('album_song', \
                db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True), \
                db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True))

# ------------------------------------------------
# Models

# Song
class Song(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    minutes = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    interpeter = db.Column(db.String(128))
    albums = db.relationship('Album', secondary='album_song', back_populates='songs')

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
    medium = db.Column(db.Enum(Medium))
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    songs = db.relationship('Song', secondary='album_song', back_populates='albums')
    __table_args__ = (db.UniqueConstraint('user', 'title', name='unique_title_for_album'), )

# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    password = db.Column(db.String(32))
    albums = db.relationship('Album', cascade='all, delete, delete-orphan')

# -------------------------------------------------------------------
# Serializers

# User
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

# Song 
class SongSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Song
        include_relationships = True
        load_instance = True 

# Album
class Enum2Dict(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'value': value.value}


class AlbumSchema(SQLAlchemyAutoSchema):
    medium = Enum2Dict(attribute='medium')
    class Meta:
        model = Album
        include_relationships = True
        load_instance =  True