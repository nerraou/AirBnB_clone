#!/usr/bin/python3
"""unit test module for BaseBase class"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel class unit test"""

    def test_wrong_constructor_args(self):
        """test wrong constructor args"""
        with self.assertRaises(TypeError):
            BaseModel(1)

    def test_doc(self):
        """test class doc"""
        self.assertGreater(len(BaseModel.__doc__), 1)
        self.assertGreater(len(BaseModel.__init__.__doc__), 1)
        self.assertGreater(len(BaseModel.__str__.__doc__), 1)
        self.assertGreater(len(BaseModel.save.__doc__), 1)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 1)

    def test_instance_creation(self):
        """test id type"""
        instance = BaseModel()
        self.assertEqual(type(instance.id), str)

    def test_save(self):
        """test save"""
        instance = BaseModel()
        checkDate = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, checkDate)

    def test__str__(self):
        """test __str__"""
        instance = BaseModel()
        string = str(instance)
        self.assertRegex(string, "^\\[BaseModel\\] \\([^)(]+\\)")

    def test_to_dict(self):
        """test to_dict"""
        instance = BaseModel()
        dictionary = instance.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
