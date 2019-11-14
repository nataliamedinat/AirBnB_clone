#!/usr/bin/python3
""" Tests Cases for the class Review """
import unittest
import pep8
from models import Review
from models.base_model import BaseModel
Review = review.Review


class Test_Review(unittest.TestCase):
    """ Tests class review """

    def test_doctring(self):
        """ Tests docstring """
        self.assertIsNotNone(review.__doc__, "Needs doctstring")

    def test_documentation(self):
        """ Test documentation """
        self.assertTrue(Amenity.__doc__, "Needs documentation")

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_child_review(self):
        """ Tests if the class User is a child class """
        review = Review()
        self.assertIsInstance(Review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id(self):
        """ Tests the attr place_id """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.review_id , " ")

    def test_user_id(self):
        """ Tests the attr user_id """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.review_id, " ")

    def test_text(self):
        """ Tests the attr text """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.asserEqual(review.text, " ")

    def test_str(self):
        """ Tests the str magic method """
        review = Review()
        result = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(result, str(Review))

    def test_to_dict_f(self):
        """ Tests the dictionary that comes from the father class """
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_to_dict_result(self):
        """ Tests the result of the dict """
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(type(new_dict["id"]), str)
