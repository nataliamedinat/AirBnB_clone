import unittest
import


class Test_Review(unittest.TestCase):
    """ Tests class review """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
