#!/usr/bin/python3
""" Tests for BaseModel. """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests for BaseModel. """
    def test_attributes(self):
        """ Test attributes base model."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_generation(self):
        """ test id generation. """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """ test created at. """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """ test updated at. """
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """ test str method. """
        model = BaseModel()
        self.assertEqual(
                str(model),
                f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}")

    def test_save_method(self):
        """ test save method. """
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """ test to dict method. """
        model = BaseModel()
        model_dic = model.to_dict()
        self.assertTrue(isinstance(model_dic, dict))
        self.assertEqual(model_dic['__class__'], 'BaseModel')
        self.assertEqual(model_dic['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dic['updated_at'], model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        """ test init with kwags. """
        data = {
            'id': 'test_id',
            'created_at': '2023-10-12T15:30:00.123456',
            'updated_at': '2023-10-12T16:45:00.789012',
            'name': 'Test Model',
            'my_number': 42,
            '__class__': 'BaseModel'
        }
        model = BaseModel(**data)

        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.my_number, 42)
        self.assertEqual(model.created_at, datetime(2023, 10, 12, 15, 30, 0, 123456))
        self.assertEqual(model.updated_at, datetime(2023, 10, 12, 16, 45, 0, 789012))

    def test_init_with_empty_kwargs(self):
        """ test init with empty kwargs. """
        model = BaseModel()
        self.assertTrue(isinstance(model.id, str))
        self.assertTrue(isinstance(model.created_at, datetime))
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_init_with_partial_kwargs(self):
        """ test init with partial kwargs. """
        data = {
            'id': 'test_id',
            'created_at': '2023-10-12T15:30:00.123456',
            'name': 'Test Model',
        }
        model = BaseModel(**data)

        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.created_at, datetime(2023, 10, 12, 15, 30, 0, 123456))
        self.assertTrue(isinstance(model.updated_at, datetime))


if __name__ == '__main__':
    unittest.main()
