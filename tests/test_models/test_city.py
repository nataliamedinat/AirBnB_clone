#!/usr/bin/python3
""" Test Cases for class city """

import unittests
import pep8
from models import import City
from models.base_model import BaseModel

class Test_City(unittest.TestCase):
    """ Tests class city """

    def test_docstring(self):
        """ Tests docstring """
        self.assertisNotNone(Amenity.__doc__)

    def test_documentation(self):
        """ Test documentation """
        self.assertTrue(Amenity.__doc__)

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_City(self):
        """ Tests if the class City is a child class """
        user = user()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at")

    def test_attrs(self):
        """ Tests the attrs """
        self.assertEqual("name", " ")
        self.assertEqual("state_id", " ")

    def test_name(self):
        """ Tests the attrs name """
        user = user()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, " ")

    def test_state_id(self):
        """ Tests the attr state_id """
        user = user()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, " ")

    def test_str(self):
        """ Tests the str magic method """
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
