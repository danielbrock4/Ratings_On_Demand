# import dependencies
from flaskr import app
# import dependencies and use Flask to render a template, redirecting to another url, and creating a URL
from flask import render_template, url_for, redirect, jsonify
import pandas as pd
from pandas import DataFrame, read_csv
from sqlalchemy import create_engine
import json 
import plotly
import plotly.express as px

# create engine to pull in data
engine = create_engine('postgresql+psycopg2://postgres:moviesondemand@moviesondemandaws.cfwjiare7kds.us-east-2.rds.amazonaws.com:5432/postgres')
# main_df = pd.read_sql_table('consolidated_pre_transformation', con=engine)

#creating global variables
global actor_df
global actor_index_df
global actor_movies

@app.route("/")
def index():
     # Graph One - Scott
    df = px.data.medals_wide()
    fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Two - Robert
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species',  title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Three - Emilio
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Graph Four - Daniel
    df = px.data.gapminder().query("continent=='Oceania'")
    fig4 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("blog/index.html", title = "Home", graph1JSON=graph1JSON,  graph2JSON=graph2JSON, 
                           graph3JSON=graph3JSON, graph4JSON=graph4JSON)

@app.route('/anIndex')
def actor_index():
    return render_template("actor_list.html", column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                           link_column="actorindex", zip=zip)