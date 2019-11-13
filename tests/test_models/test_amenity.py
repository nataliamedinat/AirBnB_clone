#!/usr/bin/python3
""" Tests Cases for class Amenity """

import unittest
import pep8
from models.basemodel import BaseModel
from models.amenity import amenity
user = user()


class Test_Amenity(unittest.TestCase):
    """ Tests the class amenity """

    def test_docstring(self):
        """ Tests """
        self.assertisNotNone(Amenity.__doc__)

    def test_pep8(self):
        """ Tests the pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(hasattr(Amenity.__doc__))
        self.assertTrue(Amenity.__doc__)
        self.assertTrue(hasattr(__init__.__doc__))
        self.assertTrue(amenity.__doc__)

    def test_child_amenity(self):
        """ Tests if th class amenity is a child class """
        user = user()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attrs(self):
        """ Tests the attr """
        self.assertEqual("name", " ")

    def test_name_attr(self):
        """ Tests the name attribute """
        user = user()
        self.assertTrue(hasattr(user, "name"))
        self.assertEqual(user.name, " ")

    def test_str(self):
        """ Tests the str magic method"""
        user = user()
        result = "[user] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(result, str(User))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class"""
        user = user()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict"""
        user = user()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
