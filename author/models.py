from flask_blog import db

# sql alchemy will map columns to this class
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True) #one email
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean) # flag - can author post vs comment
    
    # many posts by single author. Coded in author model
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __init__(self, fullname, email, username, password, is_author=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.isauthor = is_author
        
    # how class instances will apear in terminal    
    def __repr__(self):
        return '<Author %r>' % self.username