#!/usr/bin/python3
"""unit test module for City class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """City class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(City.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(City()), City)

    def test_attributes(self):
        """test attributes"""
        u = City()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.name), str)
        self.assertEqual(type(u.state_id), str)
