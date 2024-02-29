"""Unit test for Place class"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.place = Place()
        cls.place.city_id = "0001"
        cls.place.user_id = "0002"
        cls.place.name = "Holberton"
        cls.place.description = "Awesome"
        cls.place.number_rooms = 2
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 4
        cls.place.price_by_night = 100
        cls.place.latitude = 37.7749
        cls.place.longitude = 122.4194
        cls.place.amenity_ids = ["0003", "0004"]

    @classmethod
    def tearDownClass(cls):
        """Tear down for the test"""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring(self):
        """Test for docstrings"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_attributes(self):
        """Test the attributes of Place class"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
    
    def test_attributes_type(self):
        """Test the types of attributes"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
