#!/usr/bin/python3
"""unit test module for State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(State.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(State()), State)

    def test_attributes(self):
        """test attributes"""
        u = State()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.name), str)
