import unittest
import pep8
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def test_pep8_conformance_base_model(self):
        """Test that models/base_model.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring_base_model(self):
        """Test for the docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_attributes(self):
        """Test the attributes of the BaseModel class"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)

    def test_str(self):
        """Test the __str__ method"""
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string)

    def test_save(self):
        """Test the save method"""
        my_model = BaseModel()
        updated1 = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated1, my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        self.assertEqual(d["id"], my_model.id)
        self.assertEqual(d["name"], "Holberton")
        self.assertEqual(d["my_number"], 89)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["created_at"], my_model.created_at.isoformat())
        self.assertEqual(d["updated_at"], my_model.updated_at.isoformat())

    def test_init(self):
        """Test the __init__ method"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime.datetime)
        self.assertEqual(type(my_model.updated_at), datetime.datetime)
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        self.assertEqual(d["id"], my_model.id)
        self.assertEqual(d["name"], "Holberton")
        self.assertEqual(d["my_number"], 89)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["created_at"], my_model.created_at.isoformat())
        self.assertEqual(d["updated_at"], my_model.updated_at.isoformat())
