#!/usr/bin/python3
"""Module that define class FileStorage"""
import json


class FileStorage:
    """Define class FileStorage"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)