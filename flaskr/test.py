import pandas as pd
import numpy as np
import plotly
import plotly.express as px

ridge_test_results = r'static/ridge_test_results.csv'

clean_comp_results = pd.read_csv(ridge_test_results, low_memory=False)