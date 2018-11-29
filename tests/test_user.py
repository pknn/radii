from app.models import User

def test_event_password():
    u = User(username='poom1234', email='poom@example.com')
    u.set_password('mypassword')

    assert not u.check_password('anotherpassword')
    assert u.check_password('mypassword')

def test_encoding():
    u = User(username='poom1234', email='poom@example.com')
    u.set_password('mypassword')

    assert u.check_password('mypassword')
