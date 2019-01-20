
from flask import Flask, render_template
app = Flask(__name__)






@app.route('/tables')
def index():
    # student_info = (
    #    {'name' : 'Michael', 'age' : 35},
    #    {'name' : 'John', 'age' : 30 },
    #    {'name' : 'Mark', 'age' : 25},
    #    {'name' : 'KB', 'age' : 27}
    # )
    users_list = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'},
   {'first_name' : 'Carson', 'last_name' : 'f'},
   {'first_name' : 'Chris', 'last_name' : 'e'},
   {'first_name' : 'Folami', 'last_name' : 'd'},
   {'first_name' : 'Shannon', 'last_name' : 'c'},
   {'first_name' : 'Art', 'last_name' : 'b'},
   {'first_name' : 'Ash', 'last_name' : 'a'}


    )

    return render_template("htmltable.html", users = users_list)




if __name__=="__main__":
    app.run(debug=True)