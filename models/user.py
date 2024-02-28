#!/usr/bin/python3
"""Module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a user"""
    def __init__(self, *args, **kwargs):
        """Constructor of class User"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
