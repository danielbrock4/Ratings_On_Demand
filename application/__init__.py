#import dependencies and use Flask to render a template
from flask import Flask

# Set Up Flask
    # To define our Flask app we will create a Flask application called "app."
app = Flask(__name__)

from application import routes

