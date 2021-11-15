import pandas as pd
import numpy as np
import plotly
import plotly.express as px

ridge_test_results = r'C:/Users/Daniel Brock/OneDrive/Desktop/DataAnalyticsBootcamp/Final_Project/Ratings_On_Demand/flaskr/static/ridge_test_results.csv'

clean_comp_results = pd.read_csv(ridge_test_results, low_memory=False)