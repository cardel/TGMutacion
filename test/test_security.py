from unittest import TestCase
from one_conf import set_debug

class TestDatabaseFunctions(TestCase):
    
    def test_debug():
        self.assertEqual(set_debug(), True)
