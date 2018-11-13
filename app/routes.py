import os
from flask import render_template
from app import app

# from flask_login import current_user

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    return render_template("event.html", title="Event")

@app.route("/user/<username>")
def user(username):
    return render_template("user_profile.html", title="User", username=username)

