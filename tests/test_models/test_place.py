#!/usr/bin/python3
"""unit test module for Place class"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Place class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(Place.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(Place()), Place)

    def test_attributes(self):
        """test attributes"""
        u = Place()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.name), str)
