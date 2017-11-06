from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# Will decide where app run from... web, laptope etc
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
migrate = Migrate(app, db)

# Markdown
md = Markdown(app, extensions=['fenced_code', 'tables'])

# images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

# from home folder import views.py...
# keep adding folders to this?
from blog import views
from author import views
