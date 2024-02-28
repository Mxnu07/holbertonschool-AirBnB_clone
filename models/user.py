#!/usr/bin/python3
"""Module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a user"""
    def __init__(self, *args, **kwargs):
        """Constructor of class User"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('name_name', "")
        self.last_name = kwargs.get('last_name', "")
