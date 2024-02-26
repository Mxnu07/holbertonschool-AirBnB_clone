#!/usr/bin/python3
"""Module that define class BaseModel"""
import uuid
import datetime


class BaseModel:

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Constructor of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
