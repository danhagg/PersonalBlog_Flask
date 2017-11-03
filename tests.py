# This code can be reused with new apps
# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from flask_blog import app, db

# models
from author.models import *
from blog.models import *


class UserTest(unittest.TestCase):
    # temporary setup of db
    def setUp(self):
        db_username = app.config['DB_USERNAME']
        db_password = app.config['DB_PASSWORD']
        db_host = app.config['DB_HOST']
        self.db_uri = "mysql+pymysql://%s:%s@%s/" % (db_username, db_password, db_host)
        # Tells Flask its running in testing mode
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("CREATE DATABASE " + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()
        
        
    # destroy temporary db
    def tearDown(self):
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("DROP DATABASE " + app.config['BLOG_DATABASE_NAME'])
        conn.close()
    
    # create a function to make a blog for each individual test so make a function to rerun    
    def create_blog(self):
        return self.app.post('/setup', data=dict(
            name="My Test Blog",
            fullname="Daniel Haggerty",
            email="danielhaggerty1976@gmail.com",
            username="daniel",
            password="test",
            confirm="test",
            ),
        follow_redirects=True)
        
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ),
            follow_redirects=True)
            
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    
    # test_create_blog will use the create blog method to test 
    # test #1
    def test_create_blog(self):
        rv = self.create_blog()
        # print(rv.data)
        assert 'Blog created' in str(rv.data)
        # matches views.py flash('Blog created') in app.route /setup
        # and admin.html flashes
        
     
    # test #2 
    def test_login_logout(self):
        self.create_blog()
        rv = self.login('daniel', 'test')
        assert 'User daniel logged in' in str(rv.data)
        rv = self.logout()
        assert 'User logged out' in str(rv.data)
        
    #now run python tests.py    
        
if __name__ == '__main__':
    unittest.main()
    