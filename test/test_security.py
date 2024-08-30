from unittest import TestCase
from one_conf import set_SUPP_CREDENTIALS, set_TESTING_Pro, set_DEBUG_Base

class TestDatabaseFunctions(TestCase):

    def test_set_DEBUG_Base(self):
        self.assertEqual(set_DEBUG_Base(), True)

    def test_set_TESTING_Pro(self):
        self.assertEqual(set_TESTING_Pro(), False)

    def test_set_SUPP_CREDENTIALS(self):
        self.assertEqual(set_SUPP_CREDENTIALS(), True)

