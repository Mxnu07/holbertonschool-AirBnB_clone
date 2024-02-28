#!/usr/bin/python3
"""define the subclass state"""
from models.base_model import BaseModel


class State(BaseModel):
    """state where the place is"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
