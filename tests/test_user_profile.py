import unittest
from app.models import Event


class TestUserProfile(unittest.TestCase):
    def test_interested(self):
        e = Event(interested=5)
        print(e.interested_count())
        self.assertEqual(e.interested_count(), 5)

    def test_interested_is_integer(self):
        e = Event(interested=8)
        print(e.interested_count())
        self.assertEqual(e.interested_count() + 2, 10)

    def test_attending(self):
        e = Event(attending=4)
        print(e.attending_count())
        self.assertEqual(e.attending_count(), 4)

    def test_attending_is_integer(self):
        e = Event(attending=14)
        print(e.attending_count())
        self.assertEqual(e.attending_count() + 3, 17)

    def test_attended(self):
        e = Event(attended=4)
        print(e.attended_count())
        self.assertEqual(e.attended_count(), 4)

    def test_attended_is_integer(self):
        e = Event(attended=3)
        print(e.attended_count())
        self.assertEqual(e.attended_count() + 5, 8)

    # Values would be set to 0 when an invalid value is parsed in
    def test_invalid_interested_event(self):
        e = Event(interested=-5)
        print(e.interested_count())
        self.assertEqual(e.interested_count(), 0)

    def test_invalid_attending_event(self):
        e = Event(attending=-1)
        print(e.attending_count())
        self.assertEqual(e.attending_count(), 0)

    def test_invalid_attended_event(self):
        e = Event(attended=-6)
        print(e.attended_count())
        self.assertEqual(e.attended_count(), 0)
