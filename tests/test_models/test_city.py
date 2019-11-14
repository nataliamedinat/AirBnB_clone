#!/usr/bin/python3
""" Test Cases for class city """

import unittests
import pep8
from models import City
from models.base_model import BaseModel
City = city.City

class Test_City(unittest.TestCase):
    """ Tests class city """

    def test_docstring(self):
        """ Tests docstring """
        self.assertIsNotNone(amenity.__doc__, "Needs docstring")

    def test_documentation(self):
        """ Test documentation """
        self.assertTrue(amenity.__doc__, "Needs documentation")

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_City(self):
        """ Tests if the class City is a child class """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_name(self):
        """ Tests the attrs name """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id(self):
        """ Tests the attr state_id """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_str(self):
        """ Tests the str magic method """
        city = City()
        result = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(result, str(city))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
