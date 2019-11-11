#!/usr/bin/python3
""" City inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel """
    state_id = ""
    name = ""

    def __init__(*args, **kwargs):
        """ Initialization
            Attributes
                From BaseModel
        """
        super.__init__(*args, **kwargs)
