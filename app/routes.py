from flask import render_template, redirect, url_for, request, jsonify
from flask_dance.contrib.github import github
from flask_login import current_user
from app import app, auth
from app.controllers import EventController, AuthController
from app.models import Event
import sys
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "POST":
        name, description, location, image_url, date_time, category_name = (
            request.json.values()
        )
        return jsonify(
            EventController.create_event(
                name, description, location, image_url, date_time, category_name
            ).jsonify()
        )
    else:
        events = EventController.get_all_event()
        return render_template("event.html", title="Event", events=events)


@app.route("/event_dump", methods=["POST"])
def event_dump():
    dump = request.json
    return jsonify(EventController.dump_event(dump))


@app.route("/event/<event_id>")
def event_descript(event_id):
    event_info = Event.query.filter_by(event_id=event_id).first()
    return render_template("event_description.html", event_info=event_info)


@app.route("/login_github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        user_response = github.get("/user")
        user_json = user_response.json()
        AuthController.oauth(user_json["login"], user_json["email"])
        return redirect(url_for("index"))


@app.route("/register", methods=["POST"])
def register():
    display_name, email, password = request.form.values()
    AuthController.register(display_name, email, password)
    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    email, password = request.form
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    else:
        AuthController.login(email, password)
        return redirect(url_for("index"))
