#!/usr/bin/python3
"""unit test module for Review class"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(Review.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(Review()), Review)

    def test_attributes(self):
        """test attributes"""
        u = Review()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.place_id), str)
        self.assertEqual(type(u.text), str)
