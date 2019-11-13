#!/usr/bin/python3
""" Test Cases for class Place """

import unittest
import pep8
from models import place
from models.base_model import BaseModel
useer = user()


class Test_Place(unittest.TestCase):
    """ Tests Place class """

    def test_docstring(self):
        """ Tests doctring """
        self.assertisNotNone(Place.__doc__)

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(Amenity.__doc__)

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_Place(self):
        """ Tests if the class Place is a child class """
        user = user()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attrs(self):
        """ Tests the attrs """
        self.assertEqual("city_id", " ")
        self.assertEqual("user_id", " ")
        self.assertEqual("name", " ")
        self.assertEqual("description", " ")
        self.assertEqual("number_rooms", " ")
        self.assertEqual("number_bathrooms", " ")
        self.assertEqual("max_guest", " ")
        self.assertEqual("price_by_night", " ")
        self.assertEqual("latitude", " ")
        self.assertEqual("longitude", " ")
        self.assertEqual("amenity_ids", " ")

    def test_city_id(self):
        """ Tests city attr """
        user = user()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, " ")

    def test_user_id(self):
        """ Tests the attr user_id """
        user = user()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.city_id, " ")

    def test_name(self):
        """ Tests the attr name """
        user = user()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, " ")

    def test_description(self):
        """ Tests the attr description """
        user = user()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, " ")

    def test_number_rooms(self):
        """ Tests the attr number_rooms """
        user = user()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, " ")

    def test_number_bathrooms(self):
        """ Tests the attr number_bathrooms """
        user = user()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, "")

    def test_max_guest(self):
        """ Tests the attr max_guest """
        user = user()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest)

    def test_price_by_night(self):
        """ Tests the attr price_by_night """
        user = user()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night)

    def test_latitude(self):
        """ Tests the attr latitude """
        user = user()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place, latitude)

    def test_longitude(self):
        """ Tests the attr longitude """
        user = user()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place, longitude)

    def test_amenity_ids(self):
        """ Tests the attr amenity_ids """
        user = user()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place, amenity_ids)

    def test_str(self):
        """ Tests the str magic method """
        user = user()
        result = "[place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(result, str(Place))

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
