#!/usr/bin/python3
""" Tests Cases for the class Review """
import unittest
import pep8
from models import Review
from models.base_model import BaseModel
user = user()


class Test_Review(unittest.TestCase):
    """ Tests class review """

    def test_doctring(self):
        """ Tests docstring """
        self.assertisNotNone(Review.__doc__)

    def test_documentation(self):
        """ Test documentation """
        self.assertTrue(Amenity.__doc__)

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_review(self):
        """ Tests if the class User is a child class """
        user = user()
        self.assertIsInstance(User, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attrs(self):
        """ Tests attrs"""
        self.assertEqual("place_id")
        self.assertEqual("user_id")
        self.assertEqual("text")

    def test_place_id(self):
        """ Tests the attr place_id """
        user = user()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id , " ")

    def test_user_id(self):
        """ Tests the attr user_id """
        user = user()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, " ")

    def test_text(self):
        """ Tests the attr text """
        user = user()
        self.assertTrue(hasattr(review, "text"))
        self.asserEqual(review.text, " ")

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
