from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!'  # Return the string 'Hello World!' as a response.
@app.route('/play/<val1>/<val2>/<even>/<odd>')
def play(val1,val2,even,odd):
    return render_template("chess.html", val1 = int(val1), val2 = int(val2), color1 = even, color2 = odd)











if __name__=="__main__":
    app.run(debug=True)