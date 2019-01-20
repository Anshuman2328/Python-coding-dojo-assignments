from flask import Flask, render_template
app = Flask(__name__)
print(__name__)



# @app.route('/')
# def hello_world():
#     return 'Hello Flask!'  # Return the string 'Hello World!' as a response.

# def hello_world():
#     return render_template("index.html", first_name = "Ash", level = "98")
@app.route('/play/<val>')
def play(val):
    return render_template("index.html", val= int(val))

@app.route('/play/<val>/<usercolor>')
def playcolor(val, usercolor):
    return render_template("index.html", val= int(val), color = usercolor)



if __name__=="__main__":
    app.run(debug=True)