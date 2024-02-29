""" Unittest for amenity class"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.amenity

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_Amenity(self):
        """Test for docstring"""
        self.assertIsNot(Amenity.__doc__, None, "docstring")

    def test_attributes_Amenity(self):
        """Test for amenity attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """Test for is subclass"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Test for amenity attribute type"""
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "db")
    def test_save_Amenity(self):
        """Test for save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test for to_dict method"""
        self.assertEqual('to_dict' in dir(self.amenity), True)
