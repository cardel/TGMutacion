from unittest import TestCase
from one_conf import isGreater, isEq, rest

class TestDatabaseFunctions(TestCase):
    
    def test_isGreater(self):
        self.assertEqual(isGreater(5, 2), True)
    
    def test_isEq(self):
        self.assertEqual(isEq(5, 2), False)
    
    def test_rest(self):
        self.assertEqual(rest(5, 2), 3)
    