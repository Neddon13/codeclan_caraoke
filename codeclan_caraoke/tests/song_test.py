import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self): 
        self.song = ("Man, I feel like a woman!", "Shania Twain", 3)
    
    def test_does_song_have_track_number(self):
        self.assertEqual(3, self.song.track_number)  
    
