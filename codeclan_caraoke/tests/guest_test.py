import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guests = [
            { 
                "name": "Sam",
                "age": 33,
                "cash":150
            },
            {
                "name": "Daryl",
                "age": 27,
                "cash": 90
            },
            {
                "name": "Joe",
                "age": 29,
                "cash": 50
            }
        ]

    def test_does_guests_have_name(self):
        self.assertEqual("Daryl", self.guests[1]["name"])

    def test_does_guests_have_age(self):
        self.assertEqual(29, self.guests[2]["age"])

    def test_does_guests_have_cash(self):
        self.assertEqual(50, self.guests[2]["cash"])