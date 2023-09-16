#!/usr/bin/python3
"""unit test module for BaseBase class"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """BaseModel class unit test"""

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

    def test_update_class_name(self):
        """test update class name"""
        instance = BaseModel(__class__="batata",
                             id="04b54f33-14ef-4336-9f9d-d94137b7cd2d",
                             created_at="2023-09-16T14:37:56.803493",
                             updated_at="2023-09-16T14:37:56.803493")
        dictionary = instance.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertNotEqual(dictionary["__class__"], "batata")

    def test_update_missing_dates(self):
        """test update missing dates"""
        with self.assertRaises(AttributeError):
            instance = BaseModel(id="04b54f33-14ef-4336-9f9d-d94137b7cd2d")
            instance.to_dict()

    def test_deserialize(self):
        """test deserialize"""
        instance = BaseModel(id="04b54f33-14ef-4336-9f9d-d94137b7cd2d",
                             created_at="2023-09-16T14:37:56.803493",
                             updated_at="2023-09-16T14:37:56.803493")
        self.assertEqual(type(instance.created_at), datetime)
        self.assertEqual(type(instance.updated_at), datetime)
        self.assertEqual(type(instance.id), str)
