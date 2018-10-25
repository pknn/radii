import datetime
from app.models import Event,User
from app import db


def test_event_passed():
    u = Event(date_time=datetime.datetime(2018, 12, 1, 10, 30, 11))
    db.session.add(u)
    db.session.commit()

    assert not u.is_event_passed()


def test_event_upcoming():
    u = Event(date_time=datetime.datetime(2018, 9, 1, 10, 30, 11))
    db.session.add(u)
    db.session.commit()

    assert not u.is_event_upcoming()

def test_event_password():
    u = User(username='poom', email='poom@example.com')
    u.set_password('mypassword')

    assert not u.check_password('anotherpassword')
    assert u.check_password('mypassword')

def test_event_username():
    u = User(username='poom', email='poom@example.com')
    assert u