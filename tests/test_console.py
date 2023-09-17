#!/usr/bin/python3
"""unit test module for console"""


import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Console class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(HBNBCommand.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_create.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_show.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_all.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_update.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 1)
        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 1)

    def test_instance_creation(self):
        """test instance creation"""
        self.assertEqual(type(HBNBCommand()), HBNBCommand)
