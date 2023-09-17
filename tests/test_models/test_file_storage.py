#!/usr/bin/python3
"""unit test module for BaseBase class"""


import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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

    def test_instance_creation_without_args(self):
        """test instance creation without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all(self):
        """test all method"""
        TestFileStorage.save_file_storage_attrs()

        storage = FileStorage()

        objects = storage.all()
        self.assertDictEqual(objects, {})

        TestFileStorage.restore_file_storage_attrs()

    def test_all_with_args(self):
        """test all method with args"""
        with self.assertRaises(TypeError):
            storage = FileStorage()
            storage.all(1)

    def test_new_save_reload(self):
        """test save"""
        TestFileStorage.save_file_storage_attrs()

        storage = FileStorage()

        bm_obj = BaseModel()
        storage.new(bm_obj)
        storage.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(len(objects), 1)
        key = "BaseModel.{}".format(bm_obj.id)
        self.assertEqual(objects[key].id, bm_obj.id)

        TestFileStorage.restore_file_storage_attrs()

    @staticmethod
    def save_file_storage_attrs():
        """save FileStorage private attrs"""
        TestFileStorage.__original_file_path = \
            FileStorage._FileStorage__file_path
        TestFileStorage.__original_objects = \
            FileStorage._FileStorage__objects
        FileStorage._FileStorage__file_path = "tmp_test_file.json"
        FileStorage._FileStorage__objects = {}

    @staticmethod
    def restore_file_storage_attrs():
        """restore FileStorage private attrs"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass

        FileStorage._FileStorage__file_path = \
            TestFileStorage.__original_file_path
        FileStorage._FileStorage__objects = \
            TestFileStorage.__original_objects
