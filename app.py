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