import unittest
import datetime
from app.models import Event, User

class TestUserRevise(unittest.TestCase):

    def test_liked(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 123
        u = User(display_name='Poom')
        u.like(e)
        self.assertTrue(u.liked(123))

    def test_unlike(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 444
        u = User(display_name='Kevin')
        u.like(e)
        self.assertTrue(u.unlike(444))

    def test_liked_events(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 678
        u = User(display_name='Zak')

        u.like(e)
        self.assertTrue(len(u.liked_events),1)
        u.unlike(e)
        self.assertTrue(len(u.liked_events),0)

    def test_attending(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 888
        u = User(display_name='Phil')
        u.attending(e)
        self.assertTrue(u.attended(e))

    def test_unattending(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 145
        u = User(display_name='Dave')
        u.attending(e)
        self.assertTrue(u.unattending(145))

    def test_attended(self):
        e = Event(
            "test",
            "description",
            "location",
            "url",
            date_time=datetime.datetime.utcnow()
        )
        e.id = 555
        u = User(display_name='Jay')

        u.attending(e)
        self.assertEqual(len(u.attending_events),1)
        u.unattending(e)
        self.assertTrue(len(u.attending_events),0)
