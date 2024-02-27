#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = ()

def all(self):
    return self.__objects

def new(self, obj):
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    serialized_objects = ()
    for key, value in self.__objects.items():
        serialized_objects[key] = value.to_dict()
    with open(self.__file_path, "w") as file:
        json.dump(serialized_objects, file)

def reload(self):
    try:
        with open(self.__file_path, "r") as file:
            data = json.loads(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj_class = globals()[class_name]
                obj_instance = obj_class(**value)
                self.__objects[key] = obj_instance
    except FileNotFoundError:
        pass
