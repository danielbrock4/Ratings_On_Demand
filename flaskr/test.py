import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import os
from flask import Flask, request, render_template, session, redirect

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


ridge_test_results  = os.path.join("static" , "ridge_test_results.csv")
# ridge_test_results = r'static\\ridge_test_results.csvv'

# # ridge_test_results = r'C:/Users/Daniel Brock/OneDrive/Desktop/DataAnalyticsBootcamp/Final_Project/Ratings_On_Demand/flaskr/static/ridge_test_results.csv'

df = pd.read_csv(ridge_test_results, low_memory=False)
print(df)
# app = Flask(__name__, static_folder='static', static_url_path='')