import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Katy", 27, 60)

    def test_does_guest_have_name(self):
        self.assertEqual("Katy", self.guest.name)

    def test_does_guest_have_age(self):
        self.assertEqual(27, self.guest.age)