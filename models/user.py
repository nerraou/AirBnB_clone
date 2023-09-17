#!/usr/bin/python3
"""class User that inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """This is a class user that inherits from BaseMode"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
