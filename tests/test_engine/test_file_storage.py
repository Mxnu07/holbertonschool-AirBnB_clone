"""Unit test for FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8


class TestFileStorage(unittest.TestCase):
    """Test for the FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.storage

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(check.total_errors, 0, "pep8 error")

    def test_checking_for_docstring_FileStorage(self):
        """Test for docstring"""
        self.assertIsNot(FileStorage.__doc__, None, "docstring")

    def test_attributes_FileStorage(self):
        """Test for file storage attributes"""
        self.assertTrue('all' in self.storage.__dict__)
        self.assertTrue('_FileStorage__file_path' in self.storage.__dict__)
        self.assertTrue('all' in self.storage.__dict__)
        self.assertTrue('new' in self.storage.__dict__)
        self.assertTrue('save' in self.storage.__dict__)
        self.assertTrue('reload' in self.storage.__dict__)

    def test_all(self):
        """Test for all method"""
        bm = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        self.storage.new(bm)
        self.assertIn(key, self.storage.all().keys())

    def test_new(self):
        """Test for new method"""
        bm = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        self.storage.new(bm)
        self.assertIn(key, self.storage.all().keys())

    def test_save(self):
        """Test for save method"""
        bm = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        self.storage.new(bm)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test for reload method"""
        bm = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all().keys())
