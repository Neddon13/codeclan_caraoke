import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self): 
        self.song = Song("Man, I feel like a woman!", "Shania Twain")
        self.room = Room("Blue", 4, 16)

    def test_does_song_have_title(self):
        self.assertEqual("Man, I feel like a woman!", self.song.title)

    def test_does_song_have_artist(self):
        self.assertEqual("Shania Twain", self.song.artist)
        
