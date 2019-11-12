#!/usr/bin/python3
""" Amenity inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Inherits from BaseModel """
    name = ""

    def __init__(*args, **kwargs):
        """ Initialization
            Attributes
                From BaseModel
        """
        super.__init__(*args, **kwargs)
