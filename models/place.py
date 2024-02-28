#!/usr/bin/python3
"""define subclass place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place's infomation"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_nyght = 0
    latitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initialize Place"""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.amenity_ids = []
