from flask import render_template
from app import app
from app.models import User, Event
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    return render_template("event.html", title="Event")

@app.route("/event/<event_id>")
def event_descript(event_id):
    event_info = Event.query.filter_by(event_id=event_id).first()
    return render_template("event_description.html", event_info="event_info")

