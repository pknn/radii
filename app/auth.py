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
        user = User(id=user_id, username=email, email=email)
        UserController.create_user(user)
    login_user(user)
    return user


def register(form):
    print(form, file=sys.stdout)
    new_user = User(form["fullname"], form["email"], form["password"])
    db.session.add(new_user)
    db.session.commit()
    return ""
