from app.models import User

def test_event_password():
    u = User(username='poom', email='poom@example.com')
    u.set_password('mypassword')

    assert not u.check_password('anotherpassword')
    assert u.check_password('mypassword')

def test_event_username():
    u = User(username='poom', email='poom@example.com')
    assert u
