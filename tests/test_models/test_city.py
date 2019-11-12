import unittests
import


class Test_City(unittest.TestCase):
    """ Tests class city """

    def Test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

