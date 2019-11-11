#!/usr/bin/python3
""" Review inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(*args, **kwargs):
        """ Initialization
            Attributes
                From BaseModel
        """
        super.__init__(*args, **kwargs)
