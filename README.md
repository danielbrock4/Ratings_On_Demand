# **Final Project:** Ratings On Demand
Using Machine Learning to Predict IMBd Movies Scores

## Overview

Ratings on Demand is a project to predict IMDb movie ratings using features available before a movie’s release like genre, duration, budget, and Oscar nominations. Using datasets provided by [Kaggle](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset) and data we scraped from IMDb, we created a database on PostgreSQL to hold our data. Using our database and Python, we used several machine learning models such as linear and ridge regression to determine which model provided the most accurate predictions. After collecting all our results, we built a [webpage](https://ratingsondemand.herokuapp.com/) with dashboard-like features to showcase our findings to investors.

## Why Predicting Audience Ratings Would Matter to Investors

Online ratings are an indispensable part of how we watch movies. They condense an entire feature-length production into a single metric, giving us a measure by which to decide whether it's worthy of our time or not.

Audience Ratings are more than talking points; they influence the viewership of a project. National dialogue regarding movie ratings is often a massive debate topic amongst friends and social media, which may help or hurt a movie's performance at the box office. Some moviegoers go as far as solely relying on movie ratings to determine if they want to invest their time and money before they watch a movie, so investors need to try and predict movie ratings before investing in future projects. 

## **Links:**
- [Heroku Webpage](https://ratingsondemand.herokuapp.com/): Dashboard
- [Trello](https://trello.com/b/jSii2C2y/movies-on-demand): Timeline/Task Management
- [Google Slides](https://docs.google.com/presentation/d/1RqcdU3vLPqZ9CNDki9j3r28mJyeZuCQkzV43hPen5X8/edit#slide=id.gfd8f8070e1_0_106): Presentation Deck

## Questions Our Project Seeks to Answer:

* Can we accurately predict IMDb ratings with general movie variables?
  * Is our dataset sufficient enough to produce accurate film ratings? If not, what other means need to be explored?
* What correlations, if any, can be drawn between our chosen features and an accurate IMDb rating?
  * Are there any potential patterns that can be used to determine a movie's rating? For example, do movies with summer time release dates involving Oscar award winners produce play any part in a movie's IMDb rating. 
* Which Machine Learning algoriths would provide the most accurate prediction?
  * Is Linear Regression the right approach? If not, what other paths should we consider?

## Machine Learning Analysis & Results

### Feature Correlation
 - Per our observations, there were no correlations stronger than 0.50
 - The highest correlated features include
   - Duration (Minutes)
   - Is Drama Genre
   - Is Biography Genre
   - Budget (Millions)
   - Count of Oscar Nominated Actors
   - Is Comedy Genre
   - Is Horror Genre
 - Given the relatively low correlations we decided it was best to use all features in our data set for machine learning

### Feature Selected for Model
- Duration (Minutes)
- Budget (Millions)
- MPAA Rating - Utilized dummy variables
- Genres - Utilized dummy variables
- Title Length
- Month Released (Month #)
- Count of oscar nominated actors
- Oscar nominated director


### Machine Learning Model Selection
- Given that we are tying to predict a continuous dependent variable from a number f independent variables, we chose to test 3 different regression models including
 - Multiple Linear Regression
 - Ridge Regression
 - Xgboost Regression
Using R-Squared and Mean Absolute Error (MAE), Ridge regression had a slight edge over Linear Regression![image](https://user-images.githubusercontent.com/84825189/140851113-

### Machine Learning Model Results
- R Squared: .3222
- MAE: .5961


#### Actual vs Prediction Accuracy: 89.5%
 
![image](https://github.com/danielbrock4/Ratings_On_Demand/blob/read_me_updates/Images/Prediction_vs_Target_Plot.png)

#### Most Important Features

![image](https://user-images.githubusercontent.com/84825189/140852622-5bc85834-e3a8-4000-94b6-e8daac6325d0.png)

### Results Summary

- Can we accurately predict IMDb ratings with general movie attributes?
 - We are able to predict with an accuracy of 89.5%, given that it's very difficult to predict human behavior, we feel like our model provides a reasonable IMDB rating range based on a movie idea 
 

### Future Considerations

- Expand award nominations for actors and directions to include Emmy’s and Golden Globes
- Rather than utilize oscar nominated directors, utilize a top 20 list of directors as movies associated with these directors appear to get a boost in ratings regardless of other features
- Test additional regression models


## **Software:** 
**Languages and Modules**:
 - Python: 
   - Pandas, Numpy, Matplotlib, Collections, BeautifulSoup, Flask, SciPy, SQLalchemy, Plotly, PlotlyExpress
 - HTML/CSS: 
   - Bootstrap 4.0

**DataBase:** 
- PostgreSQL, QuickDBD, AWS

**Technology:** 
- JupyteLab, VS Code, Heroku, Google Slides, Slack, Zoom, Trello

**Algorithms:** 
 - Sklearn: Linear Regression, Ridge Regression
 - XGBoost

## **Data Sources:**

**Raw Data:** 
- [Kaggle](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset): IMDb movies extensive dataset

**Scraped Data**: 
- [IMDB](https://www.imdb.com/) using BeautifulSoup

