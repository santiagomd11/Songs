from flaskr import create_app
from .models import db, Song, Album, Medium, User

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# with app.app_context():
#     u = User(user_name='TEST_USER_NAME', password='TEST_PASSWORD')
#     a = Album(title='TEST_TITLE', year=1990, description='TEST_DESCRIPTION', medium=Medium.CD)
#     s = Song(title='TEST_SONG', minutes=42, seconds=42, interpeter='TEST_INTERPETER')
#     u.albums.append(a)
#     a.songs.append(s)
#     db.session.add(u)
#     db.session.add(s)
#     db.session.commit()
#     print(Album.query.all())
#     print(Album.query.all()[0].songs)
#     print(Song.query.all())
#     db.session.delete(a)
#     print(Album.query.all())
#     print(Song.query.all())