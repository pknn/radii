from app import db, login_manager
from app.models import User, Event, Category
from flask_login import login_user, logout_user


class UserController:
    @staticmethod
    def create_user(display_name, email):
        user = User(display_name, email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(id):
        return User.query.get(id)

    @staticmethod
    def get_user_liked_event(user_id):
        user = User.query.get(user_id)
        return user.liked_events


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

    @staticmethod
    def dump_event(dump):
        for i in dump:
            name, description, location, image_url, date_time, category_name = (
                i.values()
            )
            category = Category.query.filter_by(name=category_name).first()
            if category is None:
                category = Category(category_name)
                db.session.add(category)
            event = Event(name, description, location, image_url, date_time)
            category.add_event(event)
            db.session.add(event)
        db.session.commit()
        return True

    @staticmethod
    def get_all_event():
        events = Event.query.all()
        return events

    @staticmethod
    def search_by_name(query):
        events = Event.query.filter(Event.name.match(query))
        return events

    @staticmethod
    def search_by_category(query):
        category = Category.query.get(query)
        events = Event.query.filter(Event.category_id == category.id)
        return events


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class AuthController:
    @staticmethod
    def oauth(display_name, email):
        user = User.query.filter_by(display_name=display_name).first()
        if user is None:
            user = UserController.create_user(display_name, email)
        login_user(user)
        return user

    @staticmethod
    def register(display_name, email, password):
        new_user = User(display_name=display_name, email=email, password=password)
        UserController.create_user(new_user)
        return new_user

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()
        if user is None:
            return False
        else:
            if user.check_password(password):
                login_user(user)
                return True
            else:
                return False

    @staticmethod
    def logout():
        logout_user()
