#import dependencies and use Flask to render a template
from flask import Flask
import os

# Set Up Flask
    # To define our Flask app we will create a Flask application called "app."
# app = Flask(__name__)

app = Flask(__name__)

# ridge_test_results  = os.path.join("static" , "ridge_test_results.csv")

from flaskr import routes

