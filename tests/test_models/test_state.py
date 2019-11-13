#!usr/bin/python3
""" Test Cases for class State """

import unittest
import pep8
from models import State
from models.base_model import BaseModel
user = user()


class Test_State(unittest.TestCase):
    """ Tests class State """

    def test_docstring(self):
        """ Test for doctring """
        self.assertisnotNone(State.__doc__)

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(State.__doc__)

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_State(self):
        """ Tests if the class State is a child class """
        user = user()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(user, "id")
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attrs(self):
        """ Tests attrs of class State """
        self.assertEqual("name", " ")

    def test_name(self):
        """ Tests for the attr name"""
        user = user()
        self.assertTrue(hasattr(user, "name"))
        self.assertEqual(user.name, " "))

    def test_str(self):
        """ Tests str magic method """
        user = user()
        result = "[user] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(result, str(User))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        user = user()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        user = user()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
