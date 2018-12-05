from flask import render_template, redirect, url_for, request, jsonify
from flask_dance.contrib.github import github
from flask_login import current_user, login_required
from app import app, auth
from app.controllers import EventController, AuthController, CategoryController
from app.models import Event
import sys
from datetime import datetime, timedelta


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    events = EventController.get_all_event()
    categories = CategoryController.get_all_category()
    return render_template(
        "event.html",
        title="Event",
        events=events,
        categories=categories,
        current_category="All",
    )


@app.route("/browse_name", methods=["POST"])
def browse_name():
    if request.method == "POST":
        query = request.form["query"]
        events = EventController.search_by_name(query)
        return render_template("event.html", title="Event Search Result", events=events)


@app.route("/browse_category/<category_id>")
def browse_category(category_id):
    events = EventController.search_by_category_id(category_id)
    topic = CategoryController.get_name(category_id)
    categories = CategoryController.get_all_category()
    return render_template(
        "event.html",
        topic=topic,
        events=events,
        categories=categories,
        current_category=topic,
    )


@app.route("/event_dump", methods=["POST"])
def event_dump():
    dump = request.json
    return jsonify(EventController.dump_event(dump))


@app.route("/event/<int:event_id>")
def event_description(event_id):
    event_info = Event.query.get(event_id)
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
    if current_user.is_authenticated():
        return redirect(url_for("index"))
    else:
        AuthController.login(email, password)
        return redirect(url_for("index"))


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    AuthController.logout()
    return redirect(url_for("index"))


@app.route("/like/<event_id>")
def like(event_id):
    EventController.like(event_id)
    return redirect(url_for("event_description", event_id=event_id))


@app.route("/unlike/<event_id>")
def unlike(event_id):
    EventController.unlike(event_id)
    return redirect(url_for("event_description", event_id=event_id))


@app.route("/attend/<event_id>")
def attend(event_id):
    EventController.attending(event_id)
    return redirect(url_for("event_description", event_id=event_id))


@app.route("/unattend/<event_id>")
def unattend(event_id):
    EventController.unattending(event_id)
    return redirect(url_for("event_description", event_id=event_id))


@app.route("/explore")
def explore():
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
        return render_template("explore.html", title="Explore", events=events)

