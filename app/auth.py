from app.models import User
from app import login_manager
from app.controllers import UserController
from flask import redirect
from flask_login import login_user, current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def oauth(display_name, email):
    user = User.query.filter_by(display_name=display_name).first()
    if user is None:
        user = UserController.create_user(display_name, email)
    login_user(user)
    return user


def register(display_name, email, password):
    new_user = User(display_name=display_name, email=email, password=password)
    UserController.create_user(new_user)
    return new_user


def login(email, password):
    if current_user.is_authenticated:
        return redirect("/")
    user = User.query.filter_by(email=email).first()
    if user:
        if user.check_password(password):
            return user
        else:
            return None
    else:
        return None
