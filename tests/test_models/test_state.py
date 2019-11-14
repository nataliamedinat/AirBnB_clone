#!usr/bin/python3
""" Test Cases for class State """

import unittest
import pep8
from models import State
from models.base_model import BaseModel
State = state.State


class Test_State(unittest.TestCase):
    """ Tests class State """

    def test_docstring(self):
        """ Test for docstring """
        self.assertIsnotNone(state.__doc__, "Needs docstring")

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(state.__doc__, "Needs documentation")

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_State(self):
        """ Tests if the class State is a child class """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id")
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name(self):
        """ Tests for the attr name"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, ""))

    def test_str(self):
        """ Tests str magic method """
        state = State()
        result = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(result, str(State))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
