
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is my session key'
# print(__name__)
@app.route('/')
def home():
    if 'count' not in session:
        session['count'] =0
    else:
        session['count'] += 1

    return render_template("home.html")


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


@app.route('/addmore')
def addmore():
    session['count'] += 2
    return render_template("home.html")

# @app.route('/create_user', methods=['POST'])
# def create_user():
#     print(request.form)
#     session['name'] = request.form['first_name']
#     session['email'] = request.form['email']
#     return render_template("create_user.html" )
#     # return redirect ('/')









if __name__=="__main__":
    app.run(debug=True)