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
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'Chang Carnival presents The Green World Chiang Mai "Magic Mountain"',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'ห้วยตึงเฒ่า Don Kaeo, Mae Rim District, Chiang Mai, Thailand',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=20)
        },
        {
            'name': 'FitTalks',
            'description': '16-17 พฤศจิกายนนี้ ที่ ลานเนินนุ่ม ป่าขุยซิตี้',
            'location': 'โรงละครเคแบงก์สยามพิฆเนศ, ชั้น 7, Siam Square One, ถ.พระราม1 Wang Mai, Pathum',
            'image_url': 'https://p-u.popcdn.net/events/posters/000/004/394/large/EVENTPOP_POSTER_CNX.jpg?1539591838',
            'date_time': datetime.now() + timedelta(days=40)
        },
    ] 
    return render_template("event.html", title="Event", events=events)
