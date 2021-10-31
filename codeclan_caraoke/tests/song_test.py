import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self): 
        self.song1 = {"title": "Man, I feel like a woman!", "artist": "Shania Twain"}
        self.song2 = {"title": "The whole of the moon", "artist": "The Waterboys"}
        self.song3 = {"title": "Don't stop me now", "artist": "Queen"}

    def test_does_song_have_title(self):
        self.assertEqual("The whole of the moon", self.song2["title"])

    def test_does_song_have_artist(self):
        self.assertEqual("Queen", self.song3["artist"])
        
