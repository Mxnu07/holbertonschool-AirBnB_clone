#!/usr/bin/python3
"""define subclass city"""
from models.base_model import BaseModel


class City(BaseModel):
    """city where the place is"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
