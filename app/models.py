from datetime import datetime, timedelta
from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250))
    location = db.Column(db.String(100), index=True)
    image_url = db.Column(db.String(200), index=True)
    date_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

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
