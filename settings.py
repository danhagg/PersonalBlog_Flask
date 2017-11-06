import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'danhagg'
DB_PASSWORD = 'Pilky01'
BLOG_DATABASE_NAME = 'blog'
DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL:
    DB_URI = "mysql+py" + DATABASE_URL

else:
    DB_HOST = os.getenv('localhost')
    DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD,
                                              DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images'
#UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_DEST = '/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
