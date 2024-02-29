"""Unit tests for City model."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models import storage
import datetime



class TestCity(unittest.TestCase):
    """Test the City class."""
    def setUp(self):
        """Set up the tests."""
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "CA"

    def tearDown(self):
        """Tear down the tests."""
        del self.city
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_instance(self):
        """Test for correct instance creation."""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test for correct attribute assignment."""
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA")

    def test_subclass(self):
        """Test for correct inheritance."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types."""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save(self):
        """Test for correct save method."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test for correct dictionary representation."""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__,
                         'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['name'], str)
        self.assertIsInstance(city_dict['state_id'], str)

    def test_storage_var_created(self):
        """Test for storage variable creation."""
        self.assertIn(self.city, storage.all().values())

    def test_id(self):
        """Test for correct id assignment."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city2.id, str)

    def test_updated_at(self):
        """Test for correct updated_at attribute assignment."""
        city1 = City()
        old_updated_at = city1.updated_at
        city1.save()
        self.assertNotEqual(old_updated_at, city1.updated_at)
        self.assertIsInstance(city1.updated_at, datetime.datetime)

    def test_created_at(self):
        """Test for correct created_at attribute assignment."""
        city1 = City()
        city1.save()
        self.assertIsInstance(city1.created_at, datetime.datetime)
        self.assertIsInstance(city1.updated_at, datetime.datetime)

    def test_str(self):
        """Test for correct __str__ output."""
        city1 = City()
        string = "[City] ({}) {}".format(city1.id, city1.__dict__)
        self.assertEqual(string, str(city1))

    def test_kwargs(self):
        """Test for correct dictionary representation."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        city1_dict = city1.to_dict()
        city2 = City(**city1_dict)
        self.assertEqual(city1.id, city2.id)
        self.assertEqual(city1.created_at, city2.created_at)
        self.assertEqual(city1.updated_at, city2.updated_at)
        self.assertNotEqual(city1, city2)
        self.assertNotIn(city2, storage.all().values())
        city2.save()

    def test_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1), City)
        self.assertNotEqual(type(city1), BaseModel)
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city1, BaseModel)
        self.assertNotEqual(type(city1), str)
        self.assertNotEqual(type(city1), int)
        self.assertNotEqual(type(city1), list)
        self.assertNotEqual(type(city1), dict)
        self.assertNotEqual(type(city1), tuple)
        self.assertNotEqual(type(city1), set)
        self.assertNotEqual(type(city1), bool)
        self.assertNotEqual(type(city1), float)
        self.assertNotEqual(type(city1), type)
        self.assertNotEqual(type(city1), type(None))

    def test_name_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1.name), str)
        self.assertNotEqual(type(city1.name), int)
        self.assertNotEqual(type(city1.name), list)
        self.assertNotEqual(type(city1.name), dict)
        self.assertNotEqual(type(city1.name), tuple)
        self.assertNotEqual(type(city1.name), set)
        self.assertNotEqual(type(city1.name), bool)
        self.assertNotEqual(type(city1.name), float)
        self.assertNotEqual(type(city1.name), type)
        self.assertNotEqual(type(city1.name), type(None))

    def test_state_id_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1.state_id), str)
        self.assertNotEqual(type(city1.state_id), int)
        self.assertNotEqual(type(city1.state_id), list)
        self.assertNotEqual(type(city1.state_id), dict)
        self.assertNotEqual(type(city1.state_id), tuple)
        self.assertNotEqual(type(city1.state_id), set)
        self.assertNotEqual(type(city1.state_id), bool)
        self.assertNotEqual(type(city1.state_id), float)
        self.assertNotEqual(type(city1.state_id), type)
        self.assertNotEqual(type(city1.state_id), type(None))

    def test_id_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1.id), str)
        self.assertNotEqual(type(city1.id), int)
        self.assertNotEqual(type(city1.id), list)
        self.assertNotEqual(type(city1.id), dict)
        self.assertNotEqual(type(city1.id), tuple)
        self.assertNotEqual(type(city1.id), set)
        self.assertNotEqual(type(city1.id), bool)
        self.assertNotEqual(type(city1.id), float)
        self.assertNotEqual(type(city1.id), type)
        self.assertNotEqual(type(city1.id), type(None))

    def test_created_at_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1.created_at), datetime.datetime)
        self.assertNotEqual(type(city1.created_at), int)
        self.assertNotEqual(type(city1.created_at), list)
        self.assertNotEqual(type(city1.created_at), dict)
        self.assertNotEqual(type(city1.created_at), tuple)
        self.assertNotEqual(type(city1.created_at), set)
        self.assertNotEqual(type(city1.created_at), bool)
        self.assertNotEqual(type(city1.created_at), float)
        self.assertNotEqual(type(city1.created_at), type)
        self.assertNotEqual(type(city1.created_at), type(None))

    def test_updated_at_type(self):
        """Test for correct type."""
        city1 = City()
        self.assertEqual(type(city1.updated_at), datetime.datetime)
        self.assertNotEqual(type(city1.updated_at), int)
        self.assertNotEqual(type(city1.updated_at), list)
        self.assertNotEqual(type(city1.updated_at), dict)
        self.assertNotEqual(type(city1.updated_at), tuple)
        self.assertNotEqual(type(city1.updated_at), set)
        self.assertNotEqual(type(city1.updated_at), bool)
        self.assertNotEqual(type(city1.updated_at), float)
        self.assertNotEqual(type(city1.updated_at), type)
        self.assertNotEqual(type(city1.updated_at), type(None))

    def test_str_output(self):
        """Test for correct __str__ output."""
        city1 = City()
        string = "[City] ({}) {}".format(city1.id, city1.__dict__)
        self.assertEqual(string, str(city1))

    def test_save_method(self):
        """Test for correct save method."""
        city1 = City()
        old_updated_at = city1.updated_at
        city1.save()
        self.assertNotEqual(old_updated_at, city1.updated_at)
        self.assertIsInstance(city1.updated_at, datetime.datetime)

    def test_to_dict_method(self):
        """Test for correct dictionary representation."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        city1_dict = city1.to_dict()
        self.assertEqual(city1.__class__.__name__,
                         'City')
        self.assertIsInstance(city1_dict['created_at'], str)
        self.assertIsInstance(city1_dict['updated_at'], str)
        self.assertIsInstance(city1_dict['name'], str)
        self.assertIsInstance(city1_dict['state_id'], str)
        self.assertEqual(city1_dict['created_at'], city1.created_at.isoformat())
        self.assertEqual(city1_dict['updated_at'], city1.updated_at.isoformat())
        self.assertEqual(city1_dict['name'], city1.name)
        self.assertEqual(city1_dict['state_id'], city1.state_id)
        self.assertEqual(city1_dict['__class__'], 'City')

    def test_storage_all(self):
        """Test for correct storage all method."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        self.assertIn(city1, storage.all().values())

    def test_storage_new(self):
        """Test for correct storage new method."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        self.assertIn(city1, storage.all().values())

    def test_storage_save(self):
        """Test for correct storage save method."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        storage.reload()

    def test_storage_reload(self):
        """Test for correct storage reload method."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        storage.reload()

    def test_storage_get(self):
        """Test for correct storage get method."""
        city1 = City()
        city1.name = "San Francisco"
        city1.state_id = "CA"
        city1.save()
        city_id = city1.id

if __name__ == "__main__":
    unittest.main()        