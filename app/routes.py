from flask import render_template
from app import app
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():    
    return render_template("event.html", title="Event")
