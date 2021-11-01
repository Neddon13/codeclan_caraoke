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
    
    def test_has_guest_been_added_to_check_in(self):
        self.room1.add_guest_to_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.check_in))
    
    def test_add_song_to_play_list(self):
        self.room1.add_song_to_play_list(self.song2)
        self.room1.add_song_to_play_list(self.song4)
        self.room1.add_song_to_play_list(self.song3)
        self.assertEqual(3, len(self.room1.play_list))

    def test_remove_song_by_title(self):
        self.room1.play_list = [self.song1, self.song2, self.song3, self.song4]
        self.room1.remove_song_by_title("I Will Survive")
        self.assertEqual(2, len(self.room1.play_list))
