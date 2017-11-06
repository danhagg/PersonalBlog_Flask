"""
Gunicorn takes a flag, --chdir, that lets you select which directory your Python app lives in. So, if you have a directory structure like:

my-project/
  Procfile
  my_folder/
    my_module.py
and my_module.py contains:

app = Flask(__name__, ...)
You can put the following in your Procfile:

web: gunicorn --chdir my_folder my_module:app
my app = Flask(__name__, ...) is in __init__.py
"""

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_blog import app

if __name__ == "__main__":
    app.run
