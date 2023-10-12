#!/usr/bin/python3
""" test cases for amenity class. """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test amenity class cases."""
    def test_amenity_instance(self):
        """ test menity instance. """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")
