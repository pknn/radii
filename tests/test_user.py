from app.models import User

def test_event_password():
    u = User(username='poom1234', email='poom@example.com')
    u.set_password('mypassword')

    assert not u.check_password('anotherpassword')
    assert u.check_password('mypassword')

def test_event_username():
    u1 = User(username='poom1234', email='poom@example1.com')
    u2 = User(username='poom2222', email='poom@example2.com')

    assert u1.validate_username('poom1234')
    assert u2.validate_username('poom2222')

def test_encoding():
    u = User(username='poom1234', email='poom@example.com')
    u.set_password('mypassword')

    u.password_encode(u.password_hash)

    assert not u.check_password('mypassword')
