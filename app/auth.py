from app import app
from app.models import User
from app import login_manager, db
from app.controllers import UserController
from flask_login import login_user
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


def login(user_id, password):
    pass
