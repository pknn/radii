import uuid
from datetime import datetime, timedelta
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



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
