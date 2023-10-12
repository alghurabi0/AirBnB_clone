#!/usr/bin/python3
""" test cases for review class. """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ tease cases for review. """
    def test_review_instance(self):
        """ test review instance. """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")
