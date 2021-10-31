import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Blue", 4, 16)
        self.guest = Guest("Katy", 27, 60)
        self.song = Song("Man, I feel like a woman!", "Shania Twain")

    def test_does_room_have_name(self):
        self.assertEqual("Blue", self.room.name)

    def test_does_room_have_capacity(self):
        self.assertEqual(4, self.room.capacity)
    
    def test_has_guest_been_added_to_check_in(self):
        self.guest.add_guest(self.room.check_in)
        self.assertEqual(self.guest.add_guest)
