    
@app.route("/search_bar") 
def search_bar():
    return render_template("search_bar/index.html", title = "Actors & Movies Search Bar")

# @app.route('/anIndex')
# def actor_index():
#     global actor_df
#     global actor_index_df
#     global actor_movies 
#     actor_movies = pd.read_csv('static/actor_movies.csv')
#     actor_index_df= pd.read_csv('static/actor_index_df.csv')
#     actor_df= pd.read_csv('static/actor_df.csv')
#     return render_template("search_bar/index.html", title = "Actors & Movies Search Bar", column_names=actor_index_df.columns.values, row_data=list(actor_index_df.values.tolist()),
#                            link_column="actorindex", zip=zip)