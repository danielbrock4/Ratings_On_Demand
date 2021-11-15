import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import os


# ridge_test_results = r'static/ridge_test_results.csv'


ridge_test_results  = os.path.join("static" , "ridge_test_results.csv")



df = pd.read_csv(ridge_test_results, low_memory=False)
fig = px.scatter(df, x="Predicted Rating", y="Actual Rating", trendline="ols", hover_data=['Accuracy','Title', 'Genre' , 'Duration (min)' , 'Budget (mm)' , 'MPAA Rating' ])
fig.show()
