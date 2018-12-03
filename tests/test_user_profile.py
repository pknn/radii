import unittest
import datetime
from app.models import Event


class TestUserProfile(unittest.TestCase):
    def test_attending(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attending = 4
        print(e.attending_count())
        self.assertEqual(e.attending_count(), 4)

    def test_attending_is_integer(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attending = 14
        print(e.attending_count())
        self.assertEqual(e.attending_count() + 3, 17)

    def test_attended(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attended = 4
        print(e.attended_count())
        self.assertEqual(e.attended_count(), 4)

    def test_attended_is_integer(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attended = 3
        print(e.attended_count())
        self.assertEqual(e.attended_count() + 5, 8)

    def test_invalid_attending_event(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attending = -4
        print(e.attending_count())
        self.assertEqual(e.attending_count(), 0)

    def test_invalid_attended_event(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
        )
        e.attended = -6
        print(e.attended_count())
        self.assertEqual(e.attended_count(), 0)
