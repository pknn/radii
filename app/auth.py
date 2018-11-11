from app import app
from app.models import User
from app import login_manager
from app.controllers import UserController
from flask_login import login_user


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
