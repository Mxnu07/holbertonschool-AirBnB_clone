"""Unit test for User class"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestUser(unittest.TestCase):
    """Test for the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.user = User()
        cls.user.email = "betty@holberton.com"
        cls.user.password = "123"
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.user

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/user.py'])
        self.assertEqual(check.total_errors, 0, "pep8 error")

    def test_checking_for_docstring_User(self):
        """Test for docstring"""
        self.assertIsNot(User.__doc__, None, "docstring")
