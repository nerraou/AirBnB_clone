#!/usr/bin/python3
"""unit test module for User class"""


import unittest
from models.user import User
from time import sleep
from datetime import datetime


class TestUser(unittest.TestCase):
    """User class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(User.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(User()), User)

    def test_init_with_kwargs(self):
        """test init with kwargs"""
        u_ref = User()
        u_copy = User(**u_ref.to_dict())
        self.assertDictEqual(u_ref.to_dict(), u_copy.to_dict())

    def test_attributes(self):
        """test attributes"""
        u = User()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)

    def test_save(self):
        """test user save"""
        u = User()
        sleep(0.1)
        ref_updated_at = u.updated_at
        u.save()
        self.assertLess(ref_updated_at, u.updated_at)

    def test_save_with_arg(self):
        """test save with arg"""
        u = User()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_str_representation(self):
        """test str representation"""
        u = User()
        u_str = str(u)
        self.assertIn("[User] ({})".format(u.id), u_str)
        self.assertIn("'id': '{}'".format(u.id), u_str)
        self.assertIn("'created_at': " + repr(u.created_at), u_str)
        self.assertIn("'updated_at': " + repr(u.updated_at), u_str)

    def test_parent(self):
        """test parent class"""
        self.assertTrue(issubclass(User, models.base_model.BaseModel))
