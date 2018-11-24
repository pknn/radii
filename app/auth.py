from app import app
from app.models import User
from app import login_manager, db
from app.controllers import UserController
from flask_login import login_user
import sys


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def oauth(display_name, email):
    user = User.query.filter_by(display_name=display_name).first()
    if user is None:
        user = User(display_name=display_name, email=email)
        UserController.create_user(user)
    login_user(user)
    return user


def register(display_name, email, password):
    new_user = User(display_name=display_name, email=email, password=password)
    UserController.create_user(new_user)
    return new_user


def login(user_id, password):

    pass
