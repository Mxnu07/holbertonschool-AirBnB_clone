#!/usr/bin/python3
"""define subclass amenity"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """amenities of the place"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
