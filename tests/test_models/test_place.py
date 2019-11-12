import unittest

class Test_Place(unittest.TestCase):
    """ Tests Place class """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
