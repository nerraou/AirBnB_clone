#!/usr/bin/python3
"""unit test module for Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(Amenity.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(Amenity()), Amenity)

    def test_attributes(self):
        """test attributes"""
        u = Amenity()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.name), str)
