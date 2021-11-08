from flask import Flask, request,render_template
from sqlalchemy import create_engine
import pandas as pd

try: 
    engine = create_engine('postgresql+psycopg2://postgres:moviesondemand@moviesondemandaws.cfwjiare7kds.us-east-2.rds.amazonaws.com:5432/postgres')
    print("connected")
except:
    print ("I am unable to connect to the database")

#global indexActors_df
global actor_df
global actor_index_df
global actor_movies
#flask app
app = Flask(__name__)

@app.route('/')
def hello():
    try:
 #       global indexActors_df
 #       global actors_df
        global actor_df
        global actor_index_df
        global actor_movies
        actor_movies = pd.read_sql_table('actors_movies', con=engine)
        actor_index_df= pd.read_sql_table('actors_movies_index', con=engine)
        actor_df= pd.read_sql_table('actors_movies_names', con=engine)
        #the index
        # name_df= pd.DataFrame(actor_movies['actor_name'].str[0])
        # name_df['actor_name']= name_df['actor_name'].str.upper()
        # name_df.drop_duplicates(inplace=True)
        # name_df.reset_index(drop=True,inplace=True)
        #the actors
        #actor_df=pd.DataFrame(actor_movies['actor_name'])
        #actor_df['actor_name']= actor_df['actor_name'].str.upper()
        #actor_df.drop_duplicates(inplace=True)
        #actor_df.reset_index(drop=True,inplace=True)
        #actor_df.sort_values(by=['actor_name'],inplace=True)
 #       indexActors_df = pd.read_sql_table('index_4_Actors', con=engine)
 #       actors_df = pd.read_sql_table('Names', con=engine)
    except:
        return "cant retrieve data"

    return """
    <h1 style='color: red;'>Initialization</h1>
    <p>press the link to start</p>
    <a href="/anIndex">lets see an index</a>
    """

@app.route('/anIndex')
def actor_index():
    return render_template("actor_list.html", column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                           link_column="actorindex", zip=zip)

@app.route('/anActor/<string:initial>/')
def actor_initial(initial):
    initial = str.upper(initial)
    data = actor_df[['actor_name']] [actor_df['actor_name'].str.startswith('%s' % initial)].head(20)
    return render_template("actor_name.html", column_names=data.columns.values, row_data=list(data.values.tolist()),
                        link_column="actor_name", zip=zip)


@app.route('/actorlist', methods =["GET","POST"])
def actor_list():
    if request.method == "POST":
        initial = request.form.get('actorIndex')
        initial = str.upper(initial)
        data = actor_df[['actor_name']] [actor_df['actor_name'].str.startswith('%s' % initial)].head(20)
        return render_template("actorListNames.html", 
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
        return render_template("actorListNames.html", 
            column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                            link_column="actorindex",
            acolumn_names=data.columns.values, arow_data=list(data.values.tolist()),
                            alink_column="actor_name", zip=zip,t=2,nm=initial)

@app.route('/customActor', methods =["GET","POST"])
def custom_actor():
    if request.method == "POST":
        initial = request.form.get('customActor')
        data = actor_df[['actor_name']] [actor_df['actor_name'].str.contains('%s' % initial, case=False)].head(20)
        return render_template("actorListNames.html", 
            column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
                            link_column="actorindex",
            acolumn_names=data.columns.values, arow_data=list(data.values.tolist()),
                            alink_column="actor_name", zip=zip,t=1)
if __name__ == "__main__":
   app.run()