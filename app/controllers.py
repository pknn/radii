from app import db
from app.models import User, Event, Category

class UserController:
    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()

    def get_user(id):
        return User.query.get(id)

class EventController:
    @staticmethod
    def create_event(name, description, location, image_url, date_time, category_name):
        category = Category.query.filter_by(name=category_name).first()
        if category is None:
            category = Category(category_name)
            db.session.add(category)
        event = Event(name, description, location, image_url, date_time)
        category.add_event(event)
        db.session.add(event)
        db.session.commit()
        return event

