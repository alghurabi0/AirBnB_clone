#!/usr/bin/python3
""" test cases for state class. """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ test cases for state class ."""
    def test_state_instance(self):
        """ test state instance. """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")
