from app import app
from app import db


class UserController:
    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()
