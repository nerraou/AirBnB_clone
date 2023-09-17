#!/usr/bin/python3
"""File storage model"""

from json import dump, load
from models.base_model import BaseModel


class FileStorage:
    """
    This class aim to serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __classes = {"BaseModel": BaseModel}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        with key <obj class name>.id
        """
        if not obj:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to
        the JSON file (path: __file_path)
        """
        objects_dictionary = {}
        for key in FileStorage.__objects:
            obj = FileStorage.__objects[key]
            objects_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dump(objects_dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if type(FileStorage.__file_path) is not str:
            return
        try:
            with open(FileStorage.__file_path, "r",  encoding="utf-8") as file:
                objects = load(file)
                for key in objects:
                    dictionary = objects[key]
                    className = dictionary["__class__"]
                    targetClass = FileStorage.__classes[className]
                    FileStorage.__objects[key] = targetClass(**dictionary)
        except FileNotFoundError:
            pass
