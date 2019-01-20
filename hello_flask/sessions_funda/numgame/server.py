import random
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is my session key'

@app.route('/')
def index():


    session['num'] = random.randrange(0,101)

    return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
    usernum = int(request.form['userno'])
    
    if session['num'] == usernum:
        message = "you have guessed correctly"
        return render_template('results.html', message1 = message)
    else: 
        if usernum < session['num']:
            message = "you guessed incorrectly and your no is too low. The num you guessed was"     
        else:

            message = "you guessed incorrectly and your no is too high. The num you guessed was"        

        return render_template('results.html', message1 = message, num = usernum, main = session['num'] )


@app.route('/reset')
def reset():
    session.pop('num')
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    
    # take the value from user
# compare that with random num generated
# if te num is lower then random no then print too low else print too high and if the
# no is match print its a match. 
