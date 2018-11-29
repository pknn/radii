import uuid
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_login import UserMixin
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True)
    events = db.relationship("Event", backref="category")

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, id=None, display_name="", email="", password=""):
        self.display_name = display_name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"<User {self.fullname}>"

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def jsonify(self):
        object_dict = {
            "id": self.id,
            "display_name": self.display_name,
            "email": self.email,
        }
        return object_dict

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250))
    location = db.Column(db.String(100), index=True)
    image_url = db.Column(db.String(200), index=True)
    date_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    interested = db.Column(db.Integer)
    attending = db.Column(db.Integer)
    attended = db.Column(db.Integer)

    def is_event_nearby(self):
        pass
        # return Event.location

    def is_event_passed(self):
        # return true if passed and false if not
        present = datetime.utcnow()
        event = self.date_time
        if event < present:
            return True
        else:
            return False

    def is_event_upcoming(self):
        # before 3 days
        event = self.date_time
        upcoming = datetime.utcnow() + timedelta(days=3)
        if upcoming < event:
            return True
        else:
            return False

    def interested_count(self):
        if(self.interested <= 0):
            return 0
        return self.interested

    def attending_count(self):
        if (self.attending <= 0):
            return 0
        return self.attending

    def attended_count(self):
        if (self.attended <= 0):
            return 0
        return self.attended

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

