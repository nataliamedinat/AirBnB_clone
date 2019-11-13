#!/usr/bin/python3
""" Tests Cases for BaseModel """

import unittest
import pep8
from models.basemodel import base_model
from models import amenity
from models import city
from models import place
from models import review
from models import state
from models import user


class Test_Base_Model(unittest.TestCase):
    """ Test the class BaseModel father of all classes.

        Tests docstring, pep8, doc and each methodfound in the class BaseModel.
    """

    def test_docstring(self):
        """ Tests docstring of the class and methods """
        self.assertisNotNone(BaseModel.__doc__)

    def test_pep8(self):
        """ Tests pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_documentation(self):
        """  Tests documentation """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(BaseModel.to_dict.__doc__)
    
    def test_init(self):
        """ Test __init__ """
        

    def test_str(self):
        """ Test __str__"""


    def test_save(self):
        """ Test save """


    def test_to_dict(self):
        """ Test to_dict """

