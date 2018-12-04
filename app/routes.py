from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app import auth
from flask_dance.contrib.github import github
import sys
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    events = [

        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "International Accreditation for Higher Education Institutions in Thailand",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },
        {
            "name": "111",
            "description": "This seminar is designed to enhance the knowledge, understandings and importance of International Accreditation for higher education institutions in Thailand. As higher education institutions in Thailand continue to contribute to the global community of 21st Century Teaching & Learning, it is also crucial that institutions recognise the importance of becoming internationally recognised.",
            "location": "Pullman Bangkok King Power, Rang Nam Alley, Thanon Phaya Thai, Ratchathewi, Bangkok, Thailand",
            "image_url": "https://p-u.popcdn.net/events/covers/000/004/396/cover/1.png?1539833731",
            "date_time": datetime.now() + timedelta(days=20),
            "category_name": "education"
        },

        
    ]
    return render_template("event.html", title="Event", events=events)


@app.route("/login_github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        resp = github.get("/user")
        user_json = resp.json()
        print(user_json, file=sys.stdout)
        user = auth.oauth(user_json["email"])
        return jsonify(user.jsonify())


@app.route("/register", methods=["POST"])
def register():
    name, email, password = request.form
    return auth.register(name, email, password)
