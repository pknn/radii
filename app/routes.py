from flask import render_template, redirect, url_for, jsonify, request, make_response
from app import app
from app import auth
from flask_dance.contrib.github import github
import sys


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    return render_template("event.html", title="Event")


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


@app.route("/login", methods=["POST"])
def login():
    email, password = request.form
    if auth.login(email, password) == None:
        return None
