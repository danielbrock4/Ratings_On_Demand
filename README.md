# Ratings On Demand
### A Vanderbilt University Data Analytics Final Project

## Overview

Ratings on Demand is a project to predict IMDb movie ratings using features available before a movie’s release like genre, duration, budget, and Oscar nominations. Using datasets provided by [Kaggle](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset) and data we scraped from IMDb, we created a database on PostgreSQL to hold our data. Using our database and Python, we used several machine learning models such as linear and ridge regression to determine which model provided the most accurate predictions. After collecting all our results, we built a [webpage](https://ratingsondemand.herokuapp.com/) with dashboard-like features to showcase our findings to investors.

![image](https://github.com/danielbrock4/Ratings_On_Demand/blob/1707f3df539e62b0f83f132f9292281ea2b8f6c0/Images/webpage.png)

## **Links**
- [Heroku Webpage](https://ratingsondemand.herokuapp.com/): Dashboard
- [Trello](https://trello.com/b/jSii2C2y/movies-on-demand): Timeline/Task Management
- [Google Slides](https://docs.google.com/presentation/d/1RqcdU3vLPqZ9CNDki9j3r28mJyeZuCQkzV43hPen5X8/edit#slide=id.gfd8f8070e1_0_106): Presentation Deck

## Why Predicting Audience Ratings Would Matter to Investors

Online ratings are an indispensable part of how we watch movies. They condense an entire feature-length production into a single metric, giving us a measure by which to decide whether it's worthy of our time or not.

Audience Ratings are more than talking points; they influence the viewership of a project. National dialogue regarding movie ratings is often a massive debate topic amongst friends and social media, which may help or hurt a movie's performance at the box office. Some moviegoers go as far as solely relying on movie ratings to determine if they want to invest their time and money before they watch a movie, so investors need to try and predict movie ratings before investing in future projects. 

![image](Images/current_events.png)

## Questions We Seek To Answer

* Can we accurately predict IMDb ratings with general movie variables?
  * Is our dataset sufficient enough to produce accurate film ratings? If not, what other means need to be explored?
* What correlations, if any, can be drawn between our chosen features and an accurate IMDb rating?
  * Are there any potential patterns that can be used to determine a movie's rating? For example, do movies with summer time release dates involving Oscar award winners produce play any part in a movie's IMDb rating. 
* Which Machine Learning algoriths would provide the most accurate prediction?
  * Is Linear Regression the right approach? If not, what other paths should we consider?

## Process

#### Step 1 - Establish Timeline & Job Duties:
During our first week of the project, our team got together to decide on a topic. After we agreed on predicting movie scores, we established our communication would be handled via Slack and Zoom. Knowing we only had four weeks to complete the project, we created a timeline and assigned roles using Trello. Check out our Trello timeline [here](https://trello.com/b/jSii2C2y/movies-on-demand).

Every team member contributed to each phase of the project equally, but we assigned leads to each phase to be the expert in that area.
- [Team Lead & Webpage Designer](https://github.com/danielbrock4): Daniel Brock
- [Database Engineer](https://github.com/Emilio-2021): Emilio Castro
- [Machine Learning Expert](https://github.com/sbretag): Scott Bretag
- [Machine Learning Expert](https://github.com/rwalke18): Robert Walker  

![image](Images/trello.png)

#### Step 2 - Clean & Scrape Data:

#### Step 3 - Set Up Database:

#### Step 4 - Create Webpage/Dashboard

Initially, our team decided that we wanted to use Tableau to display our results. Still, after careful consideration, we decided we would have more flexibility and design control by building a webpage/dashboard. Sticking with Python being our primary coding language, creating a Flask app to run our webpage/dashboard made the most sense. Heroku provided us a free way to host a web page for our audience to access to deploy our website. 

To operate efficiently, while the database and machine learning code were being created and tested, one team member simultaneously made a simple Flask App to test deploying on Heroku. The biggest challenge we faced here was folder structure because building a webpage requires an exact folder structure to operate correctly. 

 Once the Flask App deployed successfully, we used HTML to build templates for the dashboard while we waited for machine learning code to create our visuals. After the webpage was studded and templates were set, we used CSS styling to complete the look of our page. 

Finally, after the machine learning code was completed, we added our data and visuals to our web page. Through several trial and error processes, we finally got Plotly Express to display our visuals. 

## Machine Learning Analysis & Results

### Target & Features

#### Target Variable

- IMDB Rating
  - IMDB ratings are entered by registered IMDb users who can cast a vote from 1-10 on ever released title in a database.  Individual votes are then aggregated as a signle IMDB rating, visible on the title's main page.

#### Features

- Encoded Features
  - The following features were encoded with dummy variables in order to convert to numerical values
    - MPAA Rating
      - Parental guidance rating (e.g G, PG, PG-13, R, NC-17)
    - Genres
      - e.g. Drama, Action, Mystery
      - Most movies are classified with more than 1 genre, if the movie was classified with a genre, the dummy variable would show a 1, if not, 0
  - The following features were manually ecoded during the data cleansing portion of the project
    - Count of oscar nominated actors
      - count of oscars that were previously nominated atleast once
    - Oscar nominated director
      - 1 if director was previously nominated for oscar or 0 if not
- Sourced straight from original data source
  - Duration (Minutes)
  - Budget (millions)
  - Title Length
  - Month Released (month #)

### Feature Correlation


Per our observations, there were no correlations stronger than 0.50.  In general correlations between .2 and .5 are considered to have low correlation.  Correlations below .2 are considered to have little to no correlation.  Correlation greater than .5 have a strong correlation. 
 
The highest correlated features included:
- Duration (Minutes)
- Budget (Millions)
- Count of Oscar Nominated Actors
- Drama genre
- Comedy genre
 
The visualization below shows a correlation matrix filtered with correlations greater than .2 or less than -.2

![image](Images/Corr_Matrix.png)

Given the relatively low correlations we decided it was best to use all features in our data set for machine learning model.  Note that we indentified multiple independent features that were highly correlated with each other, the risk of multicollinearity was recognized. 

### Machine Learning Model Selection
Given that we are tying to predict a continuous dependent variable from a number of independent variables, we chose to test 3 different regression models including
  - Multiple Linear Regression
  - Ridge Regression
  - Xgboost Regression

As you can see in the results below, using R-Squared and Mean Absolute Error (MAE), Ridge regression had a slight edge over Linear Regression

![image](Images/ML_Performance_Comp.png)

Ridge regression is traditionally used to model data sets that suffer from multicollinarity which we recognized in the feature correlation analysis.  Other important ridge regression features and assumptions include
  - Utilization of L2 regularization to help prevent multicollinarity
  - The assumptions of ridge regression are consistent with linear regression except for the distribution of errors to be normal need nt be assumed


### Steps take with Ridge Regression Model
- Assigned X & y variables
  - x = features mentioned above
  - y = IMdb Rating
- Train, Test, & Split
  - Test Size = 30% of data
  - Random State = 42
- Rescaled Data
  - Utilized standardscaler
- Fit model with an alpha of 10
  - The optimal alpha was identified by utilizing the RidgeCV function
- Generated predicted values from test values
- Created scatter plot to visualize the results
- Generated diagnostic plots to review model results including
  - Regression fit
  - Residual Plot
  - Normal Q-Q plot
- Created new dataframe with prediction results along with the original main data frame for further review and visualizations


### Machine Learning Model Results
- R Squared: 0.322
  - Determines how well the model captures the variance in data
- Mean Absolute Error (MAE): 0.596
  - Measures the difference between the measured value and "true" value
- Root Mean Square Error (RMSE): 0.783
  - A measure of how spread out residuals are or in other words, how concentraded the data is around the line of best fit



#### Actual vs Prediction
 
![image](Images/Prediction_vs_Target_Plot.png)

- Based on the above scatter plot, it appears that most ratings between 5 and 7 can be predicted relative accuracy shown through the tighter fit
- There appears to be a slight lean towards over predicting ratings in the 3.5-4.5 range which is most likely result of the intercept
- Taking a look at some of the larger errors using the interactive scatter plot found on our website, we identified a few trends
  - Animated films tend to be under predicted by a wide degree, two examples includ  "Up" and "Wall-E".  This potentially indicates we did not have a good feature to capture what makes an animated film better than others, futher analysis would be needed to confirm
  - Another outlier was the highest prediction the model produced which appears to be driven by the amount of actors with oscar nominations, they had more than any other movie ("Irishman") in our test data, 4 to be exact.  This feels more like a one off exception however further analysis and testing would need to be completed, this could potentially mean we need to look at different machine learning models

#### Most Important Features

The following features have been ranked by their associated coefficients to show what's most important when predicting IMDB ratings when using this particular model

![image](https://user-images.githubusercontent.com/84825189/140852622-5bc85834-e3a8-4000-94b6-e8daac6325d0.png)

## Results Summary

- Can we accurately predict IMDb ratings with general movie attributes?
 - Based on the MAE, on average we would be able to predict an IMDB rating with in
 60 bps +/- of what actual rating is or would be
 - Comparing the RMSE and MAE, the RMSE is approximately 19 bps higher than the MAE which indicates there are a few large and infrequent errors
 - Overall, it's not easy predicting human behavior but we believe that an MAE of .596 indicates that we could provide decent range of where your movie idea would fall in IMDb rating.
 

## Future Considerations

- Expand award nominations for actors and directions to include Emmy’s and Golden Globes
- Rather than utilize oscar nominated directors, utilize a top 20 list of directors as movies associated with these directors appear to get a boost in ratings regardless of other features
- Identify features to better predict animated films
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

