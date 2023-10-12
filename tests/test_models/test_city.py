#!/usr/bin/python3
""" test cases for city class. """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ test cases for ciryt. """
    def test_city_instance(self):
        """ test cases for instance city."""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
