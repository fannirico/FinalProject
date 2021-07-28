# -- Flask Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

## Additional Imports
import datetime as dt
import model as model

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = dt.datetime.now()

# -- Routes --
@app.route('/')
@app.route('/index')
def index():
    data = {
    }
    return render_template('index.html', data=data)


@app.route('/welcome', methods=["POST"])
def welcome():
    form=request.form
    name= form["name"]
    return render_template('welcome.html', name=name)

@app.route('/page1', methods=["POST", "GET"])
def page1():
    return render_template('pt1.html')

@app.route('/page2', methods=["POST", "GET"])
def page2():
    return render_template('pt2.html')

@app.route('/page3', methods=["POST", "GET"])
def page3():
    return render_template('pt3.html')

@app.route('/page4', methods=["POST", "GET"])
def page4():
    return render_template('pt4.html')

@app.route('/finish', methods=["POST", "GET"])
def finish():
    form=request.form
    name= form["name"]
    return render_template('finish.html', name=name)

# @app.route('/pt1', methods=["GET"])
# def pt1():
#     return render_template('pt1.html')