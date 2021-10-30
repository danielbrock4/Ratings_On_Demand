# import dependencies
from application import app
#import dependencies and use Flask to render a template, redirecting to another url, and creating a URL
from flask import render_template, url_for, redirect, jsonify
import pandas as pd
from pandas import DataFrame, read_csv
from sqlalchemy import create_engine
import json 
import plotly
import plotly.express as px


@app.route("/")
def index():
    return render_template("layout.html", title = "Home")