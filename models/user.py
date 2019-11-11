#!/usr/bin/python3
""" A class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(*args, **kwargs):
        """ Initialization of  father class """
        super().__init__(*args, **kwargs)
