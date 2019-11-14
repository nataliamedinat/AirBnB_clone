#!/usr/bin/python3
""" Test Cases for class Place """

import unittest
import pep8
from models import place
from models.base_model import BaseModel
Place = place.Place


class Test_Place(unittest.TestCase):
    """ Tests Place class """

    def test_docstring(self):
        """ Tests doctring """
        self.assertIsNotNone(place.__doc__, "Needs docstring")

    def test_documentation(self):
        """ Tests documentation """
        self.assertTrue(place.__doc__, "Needs documentation")

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_Place(self):
        """ Tests if the class Place is a child class """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id(self):
        """ Tests city attr """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """ Tests the attr user_id """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.city_id, "")

    def test_name(self):
        """ Tests the attr name """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description(self):
        """ Tests the attr description """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """ Tests the attr number_rooms """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, "")

    def test_number_bathrooms(self):
        """ Tests the attr number_bathrooms """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, "")

    def test_max_guest(self):
        """ Tests the attr max_guest """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, "")

    def test_price_by_night(self):
        """ Tests the attr price_by_night """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, "")

    def test_latitude(self):
        """ Tests the attr latitude """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place, latitude, "")

    def test_longitude(self):
        """ Tests the attr longitude """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place, longitude, "")

    def test_place_ids(self):
        """ Tests the attr amenity_ids """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place, place_id, "")

    def test_str(self):
        """ Tests the str magic method """
        place = Place()
        result = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(result, str(place))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
