#!/usr/bin/python3
"""unit test module for User class"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """User class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(User.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(User()), User)

    def test_attributes(self):
        """test attributes"""
        u = User()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
