import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self): 
        self.song = Song("Man, I feel like a woman!", "Shania Twain")

    def test_does_song_have_title(self):
        self.assertEqual("Man, I feel like a woman!", self.song.title)
        
