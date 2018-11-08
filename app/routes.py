from flask import render_template
from app import app
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    events =[
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '1',
            'location': '1',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '2',
            'location': '2',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '3',
            'location': '3',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '4',
            'location': '4',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '5',
            'location': '5',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '6',
            'location': '6',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '7',
            'location': '7',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '8',
            'location': '8',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '9',
            'location': '9',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '10',
            'location': '10',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '11',
            'location': '11',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '12',
            'location': '12',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '13',
            'location': '13',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '14',
            'location': '14',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '15',
            'location': '15',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16',
            'location': '16',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'FitTalks',
            'description': '17',
            'location': '17',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=40)
        },
    ] 
    return render_template("event.html", title="Event", events=events)
