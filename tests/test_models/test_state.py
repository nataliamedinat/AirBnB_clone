import unittest
import


class Test_State(unittest.TestCase):
    """ Tests class State """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
