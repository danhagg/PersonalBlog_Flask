import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'blog'
#DB_HOST = 'mysql:3306'
DB_HOST = os.getenv('localhost')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST,
                                          BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images'
#UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_DEST = '/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
