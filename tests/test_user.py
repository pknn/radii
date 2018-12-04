from app.models import User


def test_event_password():
    u = User(display_name="poom", email="poom@example.com", password="mypassword")
    assert not u.check_password("anotherpassword")
    assert u.check_password("mypassword")


def test_encoding():
    u = User(display_name="poom1234", email="poom@example.com")
    u.set_password("mypassword")

    assert u.check_password("mypassword")


def test_event_username():
    u = User(display_name="poom", email="poom@example.com")
    assert u
