from app.models import Event,User

def test_interested():
    e = Event(event_id=123, name="Lit event")
    u = User(user_id=124, username='poom')
    u.user_id = e.event_id
    u.interested
    print(u.interested_count())

def test_attending():
    pass

def test_attended():
    pass

