from flask import render_template, redirect, url_for, request, make_response
from app import app, auth
from app.models import User, Event
from datetime import datetime, timedelta
from flask_dance.contrib.github import github


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


@app.route("/login_github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        user_response = github.get("/user")
        user_json = user_response.json()
        user = auth.oauth(user_json["login"], user_json["email"])
        response = make_response(redirect(url_for("index")))
        response.set_cookie("id", str(user.id))
        response.set_cookie("email", user.email)
        return response


@app.route("/register", methods=["POST"])
def register():
    display_name, email, password = request.form.values()
    auth.register(display_name, email, password)
    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    email, password = request.form
    if auth.login(email, password) == None:
        return None
