#!/usr/bin/python3
"""defne subclass review"""


class Review(BaseModel):
    """user's review of the place"""

    place_id = ""
    user_id = ""
    text = ""
