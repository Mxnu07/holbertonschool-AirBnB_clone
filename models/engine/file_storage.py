#!/usr/bin/python3
"""file storage class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    this class represents a file storage
    system for objects in the air BnB clone project.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects currently stored."""
        return self.__objects

    def new(self, obj):
        """add a new object to storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """saves the objects to json"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """load the objects from a json"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {k: BaseModel(**v)
                                  for k, v in json.load(file).items()}
        except Exception:
            pass
