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
