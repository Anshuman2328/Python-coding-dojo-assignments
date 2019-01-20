import random
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'This is my session key'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_gold', methods = ['POST'])
def process_gold():
    if hindput == 'farm':
        fnum = random.randrange(0,31)
        session['gold'] += fnum
    else:
        session['gold'] = None
        
    return redirect ('/', total = session['gold'])


















if __name__=="__main__":
    app.run(debug=True) 
