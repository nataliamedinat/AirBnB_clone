#!/usr/bin/python3
""" State inherits from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """ Inherits from BaseModel """
    name = ""

    def __init__(*args, **kwargs):
        """ Initialization
            Attribute
                Initializates the BaseModel attrs
        """
        super.__init__(*args, **kwargs)
