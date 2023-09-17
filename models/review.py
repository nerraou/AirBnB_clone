#!/usr/bin/python3
"""class Review that inherits from BaseMode"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a class Review that inherits from BaseMode
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
