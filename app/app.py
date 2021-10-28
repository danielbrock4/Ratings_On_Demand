# # Use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, url_for, redirect, jsonify

# postgres_user = os.environ.get("POSTGRES_USER", None)

# Set Up Flask
    # To define our Flask app we will create a Flask application called "app."
app = Flask(__name__)

# Create the Welcome Route
    # Step 1: Define the welcome route 
    # Step 2: Create a function welcome() with a return statement
    # Step 3: Use f-strings to display temporaily to test app
       # When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
       # This convention signifies that this is version 1 of our application. This line can be updated to support future versions of the app as well.

# @app.route('/')
# def welcome():
#     return(
#     '''
#     Welcome to Ratings on Demand
#     Available Routes:
#     /api/v1.0/ratings
#     '''
#     )

# @app.route("/api/v1.0/ratings")
# def hello_world():
#     return "hello world"

@app.route('/')
def index():
    return render_template('base.html')

# @app.route('/get-help')
# def get_help():
#     return jsonify({"db user": postgres_user})
    
# @app.route("/api/v1.0/ratings")
# def hello_world():
#     return "hello world"


# Python program to use main for function call.
    #) It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to.
    # 1) Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
    # 2) If you import this script as a module in another script, the __name__ is set to the name of the script/module.
    # 3) Python files can act as either reusable modules, or as standalone programs.
    # 4) if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
   app.run(debug=True)
   
# Run a Flask App
    # To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code. 
    # You should save this code in the same folder you've used in the rest of this module.
        # Environment variables are essentially dynamic variables in your computer. They are used to modify the way a certain aspect of the computer operates.
        # For our FLASK_APP environment variable, we want to modify the path that will run our app.py file so that we can run our file.
        # Commands:
            # export FLASK_APP=app.py (for Mac)
            # set FLASK_APP=app.py (for PC)
            # flask run
    # Copy and paste your localhost address into your web browser. Generally, a localhost will look something like this, for context.    