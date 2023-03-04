#!/usr/bin/env python3

import sys
import os



sys.path.insert(0, '/var/www/basic-flask-app')

# Activate the virtual environment
activate_this = '/var/www/basic-flask-app/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# append the virtual environment's bin directory to the system's PATH variable
venv_bin_dir = '/var/www/basic-flask-app/venv/bin'
if venv_bin_dir not in os.environ['PATH']:
    os.environ['PATH'] += ':' + venv_bin_dir

# set the FLASK_APP and FLASK_ENV environment variables
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'development'

# import the Flask app
from app import app as application
