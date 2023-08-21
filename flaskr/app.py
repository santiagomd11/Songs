from flaskr import create_app
from .models import db, Song, Album, Medium, User

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()