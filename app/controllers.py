from app import db
from app.models import User


class UserController:
    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()

    def get_user(id):
        return User.query.get(id)
