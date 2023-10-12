#!/usr/bin/python3
""" test cases for file storage. """
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test cases  for file storage. """
    def setUp(self):
        """ set up before tests. """
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        storage.reload()

    def tearDown(self):
        """ after test is done ."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """ test all general. """
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """ test new method. """
        my_model = BaseModel()
        my_model.save()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, storage.all())

    def test_save_reload(self):
        """ test save reload methods. """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.save()
        self.assertIn(my_model, storage.all().values())

    def test_reload_no_file(self):
        """ test reload no file. """
        storage.reload()


if __name__ == '__main__':
    unittest.main()
