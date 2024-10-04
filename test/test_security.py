from unittest import TestCase
from one_conf import set_TESTING_Pro  # , set_SUPP_CREDENTIALS, set_DEBUG_Base


class TestDatabaseFunctions(TestCase):

    def test_set_TESTING_Pro(self):
        self.assertFalse(set_TESTING_Pro())
