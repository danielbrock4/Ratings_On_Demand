# import dependencies
from sklearn.linear_model import ridge_regression
from . import app
# import dependencies and use Flask to render a template, redirecting to another url, and creating a URL
#from flask import render_template, url_for, redirect, jsonify
from flask import Flask, request, render_template, session, redirect
import pandas as pd
from pandas import DataFrame, read_csv
from sqlalchemy import create_engine
import json 
import plotly
import plotly.express as px
import numpy as np
import os


# create engine to pull in data
engine = create_engine('postgresql+psycopg2://postgres:moviesondemand@moviesondemandaws.cfwjiare7kds.us-east-2.rds.amazonaws.com:5432/postgres')

#Read In Ridge Recessions Results csv
# ridge_test_results = r'static/ridge_test_results.csv'
ridge_test_results  = os.path.join(app.static_folder, "ridge_test_results.csv")

#creating global variables
global actor_df
global actor_index_df
global actor_movies
global loadedOnce

# df = pd.read_csv(ridge_test_results, low_memory=False)
# print(df)

@app.route("/")
def index():
    
    df = pd.read_csv(ridge_test_results, low_memory=False)
    fig = px.scatter(df, 
                     x="Predicted Rating", 
                     y="Actual Rating", 
                     trendline="ols", 
                     hover_data=['Accuracy','Title', 'Genre' , 'Duration (min)' , 'Budget (mm)' , 'MPAA Rating' ]
                     )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Visual
    

    #  # Graph One - Scott
    # df = px.data.medals_wide()
    # fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    # graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # # Graph Two - Robert
    # df = px.data.iris()
    # fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
    #           color='species',  title="Iris Dataset")d
    # graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # # Graph Three - Emilio
    # df = px.data.gapminder().query("continent=='Oceania'")
    # fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    # graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    # # Graph Four - Daniel
    # df = px.data.gapminder().query("continent=='Oceania'")
    # fig4 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    # graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("home/index.html", title = "Home", 
                           graphJSON=graphJSON
                        #    graph1JSON=graph1JSON,  
                        #    graph2JSON=graph2JSON, 
                        #    graph3JSON=graph3JSON, 
                        #    graph4JSON=graph4JSON
                        )
    
@app.route("/search_bar") 
def search_bar():
    loadedOnce=False
    if loadedOnce==False:
        global actor_df
        global actor_index_df
        global actor_movies 
        target = os.path.join(app.static_folder, 'actor_movies.csv')
        #print(target)
        actor_movies = pd.read_csv(target)
        target = os.path.join(app.static_folder, 'actor_index_df.csv')
        actor_index_df= pd.read_csv(target)
        target = os.path.join(app.static_folder, 'actor_df.csv')
        actor_df= pd.read_csv(target)
        loadedOnce=True
    return render_template("search_bar/index.html", title = "Actors & Movies Search Bar", column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                           link_column="actorindex", zip=zip)

@app.route('/actorlist', methods =["GET","POST"])
def actor_list():
    if request.method == "POST":
        initial = request.form.get('actorIndex')
        initial = str.upper(initial)
        data = actor_df[['actor_name']] [actor_df['actor_name'].str.startswith('%s' % initial)].head(20)
        return render_template("search_bar/actorListNames.html", 
            column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                            link_column="actorindex",
            acolumn_names=data.columns.values, arow_data=list(data.values.tolist()),
                            alink_column="actor_name", zip=zip,t=1)

@app.route('/movielist', methods =["GET","POST"])
def movie_list():
    if request.method == "POST":
        initial = request.form.get('actorName')
        #initial = str.upper(initial)
        data = actor_movies[['movie_title']] [actor_movies['actor_name'].str.contains('%s' % initial)].head(20)
        return render_template("search_bar/actorListNames.html", 
            column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                            link_column="actorindex",
            acolumn_names=data.columns.values, arow_data=list(data.values.tolist()),
                            alink_column="actor_name", zip=zip,t=2,nm=initial)

@app.route('/customActor', methods =["GET","POST"])
def custom_actor():
    if request.method == "POST":
        initial = request.form.get('customActor')
        data = actor_df[['actor_name']] [actor_df['actor_name'].str.contains('%s' % initial, case=False)].head(20)
        return render_template("search_bar/actorListNames.html", 
            column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                            link_column="actorindex",
            acolumn_names=data.columns.values, arow_data=list(data.values.tolist()),
                            alink_column="actor_name", zip=zip,t=1)
        
