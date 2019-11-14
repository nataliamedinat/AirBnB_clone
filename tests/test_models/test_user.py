8#!/usr/bin/python3
""" Tests Cases for the class User """
import unittest
import pep8
from models import user
from models.base_model import BaseModel
User = user.User


class Test_User(unittest.TestCase):
    """ Tests class user """

    def test_docstring(self):
        """ Tests doctring """
        self.assertIsNotNone(user.__doc__, "Needs docstring")

    def test_documentation(self):
        """ Test for documentatio """
        self.assertTrue(user.__doc__, "Needs documentation")

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_User(self):
        """ Tests if the class User is a child class """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email(self):
        """ Tests email attr """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """ Tests the password attr """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """ Tests the first name attr """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """ Tests the last name attr """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """ Tests str magic method """
        user = User()
        result = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(result, str(user))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
