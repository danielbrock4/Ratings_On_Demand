# from application tells to app is run from the application folder
# import app run.py to run app from __init__.py
from flaskr import app

if __name__ == '__main__':
    app.run(debug=True)