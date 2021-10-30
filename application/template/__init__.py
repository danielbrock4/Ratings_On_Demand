#import dependencies and use Flask to render a template
from flask import Flask, render_template, url_for, redirect, jsonify
import pandas as pd
import numpy as np
from pandas import DataFrame, read_csv
from sqlalchemy import create_engine


# Set Up Flask
    # To define our Flask app we will create a Flask application called "app."
app = Flask(__name__)

from application import routes

