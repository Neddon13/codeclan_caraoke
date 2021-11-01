import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("I will Survive", "Gloria Gaynor")
        self.song2 = Song("Man, I Feel Like a Woman!", "Shania Twain")
        self.song3 = Song("The Whole of The Moon", "The Waterboys")
        self.song4 = Song("Brown Eyed Girl", "Van Morrison")

    def test_does_song_have_title(self):
        self.assertEqual("Man, I Feel Like a Woman!", self.song2.title)

    def test_does_song_have_artist(self):
        self.assertEqual("Van Morrison", self.song4.artist)
        
