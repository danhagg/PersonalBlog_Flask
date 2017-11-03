# this decorator is in blog views.py file
from functools import wraps
from flask import session, request, redirect, url_for, abort

# login required for users to post comments
def login_required(f): # we subclass from function 'f'
    @wraps(f)
    # login reqd page may be called from any page, 
    # thus, needs to return u back to that page after login
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
    
# A different decorator for authors to be logged in
def author_required(f): # we subclass from function 'f'
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('is_author') is None:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function