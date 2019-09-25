from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")
