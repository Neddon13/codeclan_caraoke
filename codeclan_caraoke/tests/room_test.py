import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Blue", 4, 16)
        self.room2 = Room("Green", 5, 18)
        self.guest1 = Guest("Katy", 27, 60)
        self.guest2 = Guest("Laura", 25, 10)
        self.guest3 = Guest("Craig", 28, 40)
        self.guest4 = Guest("Joe", 17, 15)
        self.guest5 = Guest("Tom", 24, 5)
        self.song1 = Song("I Will Survive", "Gloria Gaynor")
        self.song2 = Song("Man, I Feel Like a Woman!", "Shania Twain")
        self.song3 = Song("The Whole of The Moon", "The Waterboys")
        self.song4 = Song("Brown Eyed Girl", "Van Morrison")

    def test_does_room_have_name(self):
        self.assertEqual("Blue", self.room1.name)

    def test_does_room_have_capacity(self):
        self.assertEqual(5, self.room2.capacity)
    
    def test_has_guest_checked_in(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_in_guest(self.guest3)
        self.assertEqual(3, len(self.room1.check_in))
    
    def test_does_guest_have_sufficient_funds(self):
        self.guest1.check_guest_has_enough_cash(self.room1)
        self.assertEqual(True, self.guest1.cash)
