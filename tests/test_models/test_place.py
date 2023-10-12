#!/usr/bin/python3
""" test cases for place class. """
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ test cases for place. """
    def test_place_instance(self):
        """ tesst place instance. """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
