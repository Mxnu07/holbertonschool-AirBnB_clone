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

    def test_save_no_args(self):
        """Test for save method with no arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_save_many_args(self):
        """Test for save method with many arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(1, 2)

    def test_reload_no_args(self):
        """Test for reload method with no arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    def test_reload_many_args(self):
        """Test for reload method with many arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(1, 2)

    def test_new_no_args(self):
        """Test for new method with no arguments"""
        with self.assertRaises(TypeError):
            self.storage.new(None)

    def test_new_many_args(self):
        """Test for new method with many arguments"""
        with self.assertRaises(TypeError):
            self.storage.new(1, 2)

    def test_all_no_args(self):
        """Test for all method with no arguments"""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_all_many_args(self):
        """Test for all method with many arguments"""
        with self.assertRaises(TypeError):
            self.storage.all(1, 2)

    def test_save(self):
        """Test for save method"""
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test for reload method"""
        self.storage.reload()
        self.assertTrue(os.path.exists('file.json'))
        self.assertEqual(type(self.storage.all()), dict)
        self.assertEqual(len(self.storage.all()), 0)
        self.assertEqual(self.storage._FileStorage__objects, {})
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "all"))
        self.assertTrue(hasattr(self.storage, "new"))
        self.assertTrue(hasattr(self.storage, "save"))
        self.assertTrue(hasattr(self.storage, "reload"))

    def test_save_no_args(self):
        """Test for save method with no arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(None)
