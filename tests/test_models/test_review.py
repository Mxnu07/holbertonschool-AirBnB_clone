"""Unit test for Review class"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.review = Review()
        cls.review.place_id = "123"
        cls.review.user_id = "123"
        cls.review.text = "Great place"

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.review

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/review.py'])
        self.assertEqual(check.total_errors, 0, "pep8 error")

    def test_checking_for_docstring_Review(self):
        """Test for docstring"""
        self.assertIsNot(Review.__doc__, None, "docstring")

    def test_attributes_Review(self):
        """Test for review attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_is_subclass_Review(self):
        """Test for is subclass"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)
