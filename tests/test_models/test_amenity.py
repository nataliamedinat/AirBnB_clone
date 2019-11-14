#!/usr/bin/python3
""" Tests Cases for class Amenity """

import unittest
import pep8
from models.base_model import BaseModel
from models import amenity
Amenity = amenity.Amenity


class Test_Amenity(unittest.TestCase):
    """ Tests the class amenity """

    def test_docstring(self):
        """ Tests """
        self.assertIsNotNone(amenity.__doc__, "Needs docstring")

    def test_pep8(self):
        """ Tests the pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(amenity.__doc__, "Needs documentation")

    def test_child_amenity(self):
        """ Tests if th class amenity is a child class """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_attrs(self):
        """ Tests the attr """
        self.assertEqual("name", " ")

    def test_name_attr(self):
        """ Tests the name attribute """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """ Tests the str magic method"""
        amenity = Amenity()
        result = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(result, str(amenity))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
