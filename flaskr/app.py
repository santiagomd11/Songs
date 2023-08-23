from flaskr import create_app
from .models import db, Song, Album, Medium, User
from .models import AlbumSchema, SongSchema, UserSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    song_schema = SongSchema()
    s = Song(title='TEST_TITLE', minutes=42, seconds=42, interpeter='TEST_INTERPETER')
    db.session.add(s)
    db.session.commit()
    print([song_schema.dumps(song) for song in Song.query.all()])