"""Unit test for State class"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.state

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_State(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/state.py'])
        self.assertEqual(check.total_errors, 0, "pep8 error")

    def test_checking_for_docstring_State(self):
        """Test for docstring"""
        self.assertIsNot(State.__doc__, None, "docstring")

    def test_attributes_State(self):
        """Test for state attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """Test for is subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """Test for the attribute type of State"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """Test for save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test for to_dict method"""
        self.assertEqual('to_dict' in dir(self.state), True)
