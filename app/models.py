from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True)
    events = db.relationship("Event", backref="category")

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def add_event(self, event):
        self.events.append(event)

    def jsonify(self):
        return {"name": self.name, "events": self.events}


user_liked_event = db.Table(
    "user_liked_event",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)

user_attending_event = db.Table(
    "user_attending_event",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)

user_attended_event = db.Table(
    "user_attended_event",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250))
    location = db.Column(db.String(100), index=True)
    image_url = db.Column(db.String(200), index=True)
    date_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))

    liked_users = db.relationship(
        "User", secondary=user_liked_event, back_populates="liked_events"
    )
    attending_users = db.relationship(
        "User", secondary=user_attending_event, back_populates="attending_events"
    )
    attended_users = db.relationship(
        "User", secondary=user_attended_event, back_populates="attended_events"
    )

    def __init__(self, name, description, location, image_url, date_time):
        self.name = name
        self.description = description
        self.location = location
        self.image_url = image_url
        self.date_time = date_time

    def jsonify(self):
        return {
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "image_url": self.image_url,
            "date_time": self.date_time,
            "category_id": self.category_id,
        }

    def is_event_passed(self):
        present = datetime.utcnow()
        event = self.date_time
        if event < present:
            return True
        else:
            return False

    def is_event_upcoming(self):
        event = self.date_time
        upcoming = datetime.utcnow() + timedelta(days=3)
        if upcoming < event:
            return True
        else:
            return False

    def interested_count(self):
        return len(self.liked_users)

    def attending_count(self):
        if self.attending <= 0:
            return 0
        return self.attending

    def attended_count(self):
        if self.attended <= 0:
            return 0
        return self.attended


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    liked_events = db.relationship(
        "Event", secondary=user_liked_event, back_populates="liked_users"
    )
    attending_events = db.relationship(
        "Event", secondary=user_attending_event, back_populates="attending_users"
    )
    attended_events = db.relationship(
        "Event", secondary=user_attended_event, back_populates="attended_users"
    )

    def __init__(self, display_name="", email="", password=""):
        self.display_name = display_name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"<User {self.display_name}>"

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

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def like(self, event):
        self.liked_events.append(event)

    def unlike(self, event_id):
        for event in self.liked_events:
            if event.id == event_id:
                self.liked_events.remove(event)
                return True
        else:
            return False

    def liked(self, event_id):
        for event in self.liked_events:
            if event.id == event_id:
                return True
        else:
            return False

    def attending(self, event):
        self.attending_events.append(event)

    def unattending(self, event_id):
        for event in self.attending_events:
            if event.id == event_id:
                self.attending_events.remove(event)
                return True
        else:
            return False

    def attended(self, event):
        if self.unattending(event.id):
            self.attended_events.append(event)
            return True
        else:
            return False


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
