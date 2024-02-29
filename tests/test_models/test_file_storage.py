"""Unit test for FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
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
        """Test for FileStorage attributes"""
        self.assertTrue('all' in self.storage.__dict__)
        self.assertTrue('new' in self.storage.__dict__)
        self.assertTrue('save' in self.storage.__dict__)
        self.assertTrue('reload' in self.storage.__dict__)
        self.assertTrue('_FileStorage__file_path' in self.storage.__dict__)
        self.assertTrue('_FileStorage__objects' in self.storage.__dict__)

    def test_all(self):
        """Test for all method"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """Test for new method"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 12345
        user.name = "Betty"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload(self):
        """Test for reload method"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 12345
        user.name = "Betty"
        key = user.__class__.__name__ + "." + str(user.id)
        obj[key] = user
        storage.reload()
        self.assertIsNotNone(obj[key])

    def test_save(self):
        """Test for save method"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 12345
        user.name = "Betty"
        key = user.__class__.__name__ + "." + str(user.id)
        obj[key] = user
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
