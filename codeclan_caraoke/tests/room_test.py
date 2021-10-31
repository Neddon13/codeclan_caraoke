import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = {"name": "Blue", "Capacity": 2}
        self.room2 = {"name": "Green", "Capacity": 3}
        self.room3 = {"name": "Red", "Capacity": 5}

    def test_does_room_have_name(self):
        self.assertEqual("Blue", self.room1["name"])

    def test_does_room_have_capacity(self):
        self.assertEqual(3, self.room2["Capacity"])

