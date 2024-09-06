from unittest import TestCase
from one_conf import set_SUPP_CREDENTIALS, set_TESTING_Pro, set_DEBUG_Base


class TestDatabaseFunctions(TestCase):

    def test_set_DEBUG_Base(self):
        self.assertTrue(set_DEBUG_Base())

    def test_set_TESTING_Pro(self):
        self.assertFalse(set_TESTING_Pro())

    def test_set_SUPP_CREDENTIALS(self):
        self.assertTrue(set_SUPP_CREDENTIALS())
