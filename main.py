######################################################################
#                                                                    #
#   Name: Seyyed Sadegh Hosseini                                     #
#   Project: Numbers Puzzle (AI First Project)                       #
#   Teacher: Dr. Hossein Ebrahimpour                                 #
#   Date: 2019-Oct-24                                                #
#                                                                    #
######################################################################

from flask import Flask, render_template
from flaskwebgui import FlaskUI
from init import init
from solve_puzzle import solve_puzzle

app = Flask(__name__)
ui = FlaskUI(app)


d = init()


@app.route("/")
def index():
    return render_template("index.html", data=d)


@app.route("/solve")
def solve():
    solved = solve_puzzle(d)
    return render_template("solve.html", data=solved)



ui.run()
