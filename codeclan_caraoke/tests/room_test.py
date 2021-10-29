import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Blue", 12)
        self.guest = Guest("Sam", 33, 150)

    def test_does_room_have_name(self):
        self.assertEqual("Blue", self.room.name)

    def test_does_room_have_capacity(self):
        self.assertEqual(12, self.room.capacity)
