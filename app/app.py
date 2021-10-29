# # Use Flask to render a template, redirecting to another url, and creating a URL
from email import header
from flask import Flask, render_template, url_for, redirect, jsonify
import pandas as pd
import numpy as np
from pandas import DataFrame, read_csv
from sqlalchemy import create_engine


# Set Up Flask
    # To define our Flask app we will create a Flask application called "app."
app = Flask(__name__)



engine = create_engine('postgresql+psycopg2://postgres:moviesondemand@moviesondemandaws.cfwjiare7kds.us-east-2.rds.amazonaws.com:5432/postgres')
main_df = pd.read_sql_table('consolidated_pre_transformation', con=engine)


@app.route('/')
def index():
    return render_template('base.html', tables=[main_df.to_html()], titles= ["na"])


# Python program to use main for function call.
    #) It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to.
    # 1) Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
    # 2) If you import this script as a module in another script, the __name__ is set to the name of the script/module.
    # 3) Python files can act as either reusable modules, or as standalone programs.
    # 4) if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
   app.run(debug=True)