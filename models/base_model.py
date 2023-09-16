#!/usr/bin/python3
"""Defines a base class BaseModel"""


import uuid
from datetime import datetime


class BaseModel():
    """This is Base model of all commig model"""
    def __init__(self):
        """ init base model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """return: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        and __class__
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = BaseModel.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
