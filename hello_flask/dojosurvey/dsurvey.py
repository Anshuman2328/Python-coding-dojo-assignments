

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("dsurvey.html")
# this route will handle our form submission
@app.route('/surveyresult', methods=['POST'])
def create_user():
    print("Got Post Info")
    namefromform = request.form['thisismyname']
    emailfromform = request.form['thisismyemail']
    locationfromform = request.form["locations"]
    languagesfromform = request.form["languages"]
    commentfromform = request.form["comments"]
    return render_template("dsurvey2.html", nametojinja = namefromform, emailtojinja = emailfromform, locationtojinja = locationfromform, languagestoninja = languagesfromform, comtojinja = commentfromform )


if __name__=="__main__":
    app.run(debug=True) 
