import unittest

class Test_Amenity(unittest.TestCase):
    """ Tests the class amenity """

    def Test_docstring(self):
        """ Tests """

    def Test_pep8(self):
        """ Tests the pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def Test_(self):
        """ Tests """

    def Test_(self):
        """ Tests """

    def Test_(self):
        """ Tests """

    def Test_(self):
        """ Tests """
