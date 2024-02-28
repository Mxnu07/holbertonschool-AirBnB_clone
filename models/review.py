#!/usr/bin/python3
"""defne subclass review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """user's review of the place"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review instance"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
