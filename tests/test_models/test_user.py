import unittest
import pep8


class Test_User(unittest.TestCase):
    """ Tests class user """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_error, 0, "Fix pep8")
