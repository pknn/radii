import uuid
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True)
    events = db.relationship('Event', backref='category')

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

interested_events = db.Table('interested_events',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.event_id'))
)

attending_events = db.Table('attending_events',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.event_id'))
)

attended_events = db.Table('attended_events',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.event_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    interested = db.relationship('Event', secondary=interested_events, backref=db.backref('interest',lazy='dynamic'))
    attending = db.relationship('Event', secondary=attending_events, backref=db.backref('attending',lazy='dynamic'))
    attended = db.relationship('Event', secondary=attended_events, backref=db.backref('attended',lazy='dynamic'))

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def interested_count(self):
        return len(self.interested)

    def attending_count(self):
        return len(self.attending)

    def attended_count(self):
        return len(self.attended)

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250))
    location = db.Column(db.String(100), index=True)
    image_url = db.Column(db.String(200), index=True)
    date_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


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
