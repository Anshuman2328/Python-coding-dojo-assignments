
from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return render_template("index.html") # Return the string 'Hello World!' as a response.


# @app.route('/Dojo')
# def name():
#     return "Dojo"


# @app.route('/say/<name>')
# def say(name):
#     print("\n\n\n*****************handle this routing request*****************")
#     return "Hi " + name 


# @app.route('/repeat/<val>/<name>')
# def repeat(val,name):
#     print("\n\n\n*****************handle this routing request*****************")
#     return int(val) *  name   












if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
