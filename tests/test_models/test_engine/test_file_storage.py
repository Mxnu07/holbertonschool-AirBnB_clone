import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_quit(None))
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_EOF(None))
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.hbnb_command.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)
        # Aquí puedes agregar más aserciones para verificar el comportamiento esperado

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        with patch.dict(storage.all(), {"BaseModel.1234": "test_object"}):
            self.hbnb_command.do_show("BaseModel 1234")
            self.assertEqual(mock_stdout.getvalue().strip(), "test_object")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        with patch.dict(storage.all(), {"BaseModel.1234": "test_object"}):
            self.hbnb_command.do_destroy("BaseModel 1234")
            self.assertNotIn("BaseModel.1234", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        with patch.dict(storage.all(), {"BaseModel.1234": "test_object1", "BaseModel.5678": "test_object2"}):
            self.hbnb_command.do_all("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("test_object1", output)
            self.assertIn("test_object2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        with patch.dict(storage.all(), {"BaseModel.1234": "test_object"}):
            self.hbnb_command.do_update("BaseModel 1234 name 'new_name'")
            updated_object = storage.all()["BaseModel.1234"]
            self.assertEqual(updated_object.name, "new_name")

if __name__ == '__main__':
    unittest.main()
