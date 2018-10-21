from flask import render_template
from app.models import Event
from app import app
from datetime import datetime, timedelta

@app.route('/')
def index():
    return render_template('index.html', title='Coming soon')

@app.route('/event')
def event():

    events = [
        {
            'name': 'SWU OPEN HOUSE 2018 - เปิดบ้านศรีนครินทรวิโรฒ 2561',
            'description': 'description 1#',
            'location': 'มหาวิทยาลัยศรีนครินทรวิโรฒ ประสานมิตร กรุงเทพมหานคร',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow()  +timedelta(days=5)
        },
        {
            'name': 'Thailand Top 100 by JOOX',
            'description': 'description 2#',
            'location': ' OASIS SHOW DC, Huai Khwang, Bang Kapi, Bangkok, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow() + timedelta(days=7)
        },
        {
            'name': 'Chang Carnival presents The Green World Bangkok "Urban Jungle',
            'description': 'description 3#',
            'location': ' Hall 98, BITEC Bang Na, Bang Na, Bangkok, Thailand ',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow() + timedelta(days=10)
        },
        {
            'name': 'OMG - Oh My Ghost',
            'description': 'description 4#',
            'location': 'Live Park (Rama 9), Bang Kapi, Huai Khwang, Bangkok, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow() + timedelta(days=11)
        },
        {
            'name': 'MUI FEST 2018',
            'description': 'description 5#',
            'location': 'W Koh Samui, Mae Nam, Ko Samui District, Surat Thani, Thailand ',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow() + timedelta(days=12)
        },
        {
            'name': 'WHITE PARTY BANGKOK',
            'description': 'description 5#',
            'location': 'GMM Live House at CentralWorld & So Sofitel Bangkok',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/003/845/large/1539241641076.jpg?1539681246',
            'date_time': datetime.utcnow() + timedelta(days=15)
        }
    ]

    return render_template('event.html', title="Event", events=events)