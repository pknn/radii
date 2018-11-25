from app import app
from app.models import User
from app import login_manager, db
from app.controllers import UserController
from flask import render_template, redirect, url_for
from flask_login import login_user, current_user
import sys


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def oauth(user_id, email):
    user = User.query.get(user_id)
    if user is None:
        user = User(id=user_id, fullname=email, email=email)
        UserController.create_user(user)
    login_user(user)
    return user


def register(name, email, password):
    new_user = User(name, email, password)
    UserController.create_user(new_user)
    return new_user


def login(email, password):
    if current_user.is_authenticated:
        return redirect('/')
    user = User.query.filter_by(email=email).first()
    if user:
        if user.check_password(password):
            return user
        else:
            return None
    else:
        return None
