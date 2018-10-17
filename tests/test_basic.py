import pytest
from app.models import User
from app import db


def test_simple():
    user = User(username="Pakanon")
    db.session.add(user)
    db.session.commit()

    user = User.query.all()[0]
    db.session.delete(user)
    db.session.commit()
    assert 2 + 3 == 5
