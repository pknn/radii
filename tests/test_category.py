from app.models import Category


def test_id():
    c = Category(name="Poom")

    print(c.get_id())
    assert c.get_id() is None


def test_name():
    c = Category(name="Benz")

    print(c.get_name())
    assert c.get_name()
