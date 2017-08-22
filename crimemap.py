from dbheler import DBHElper
from flask import Flask
from flask import render_template
from flask import request

#Importing chunck.


app = Flask(__name__)
DB = DBHelper()

#Initializing initial variables.


@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=data)

#Defining home function and routing "/"


@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print # coding=utf-8
    return home()

#Defining add function and routing "/add"


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

#Defining clear function and routing "/clear"


if __name__ == '__main__':
    app.run(port=5000, debug=True)

#Running the app at port 5000
