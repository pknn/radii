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

@app.route("/event/info")
def event_description():
    event_info = {
            'name': 'WHITE PARTY BANGKOK',
            'description': 'WHITE PARTY BANGKOK returns with another awesome New Year Festival from 28 - 31 Dec 2018. There will be 5 massive parties spanning over 4 days with a huge list of the HOTTEST international DJs and performers. Over 15,000 guys are expected to attend this year; making WHITE PARTY BANGKOK the BIGGEST gay New Year festival in Asia and one of the BIGGEST circuit festivals in the world!',
            'location': 'GMM Live House at CentralWorld & So Sofitel Bangkok',
            'image_url': 'https://p-u.popcdn.net/events/covers/000/003/801/cover/KeyVisual_%28851x400%29with_S.png?1532339133',
            'date_time': datetime.now() + timedelta(days=20)
    }
    user = {'username': 'Miguel'}
    return render_template("event_description.html", event_info=event_info )
