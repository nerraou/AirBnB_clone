#!/usr/bin/python3
"""unit test module for BaseBase class"""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """FileStorage class unit test"""

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(FileStorage.__doc__), 1)
        self.assertGreater(len(FileStorage.all.__doc__), 1)
        self.assertGreater(len(FileStorage.new.__doc__), 1)
        self.assertGreater(len(FileStorage.reload.__doc__), 1)
        self.assertGreater(len(FileStorage.save.__doc__), 1)

    def test_instance_creation_with_args(self):
        """test instance creation with args"""
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_all(self):
        """test all method"""
        orignal_file_path = FileStorage._FileStorage__file_path

        FileStorage._FileStorage__file_path = "/tmp/tmp_test_file.json"
        FileStorage._FileStorage__file_path = orignal_file_path
