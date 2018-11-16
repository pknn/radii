import os
from flask import render_template
from app import app, db
from app.models import User
from datetime import datetime, timedelta
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    return render_template("event.html", title="Event")

@app.route("/user/<username>")
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()    
    attending_len = User.attending_count(user)
    attended_len = User.attended_count(user)
    interested_len = User.interested_count(user)
    return render_template("user_profile.html", title="User", user=user, attending_len=attending_len, attended_len=attended_len, interested_len=interested_len)    

