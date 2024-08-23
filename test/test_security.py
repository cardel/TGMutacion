from unittest import TestCase
from one_conf import get_DEBUG_DevConfig, get_DEBUG_BaseConfig, get_DEBUG_ProConfig, get_MAX_AGE_CORSConfig

class TestDatabaseFunctions(TestCase):
    
    def test_get_DEBUG_DevConfig(self):
        self.assertEqual(get_DEBUG_DevConfig(), True)
    
    def test_get_DEBUG_BaseConfig(self):
        self.assertNotEqual(get_DEBUG_BaseConfig(), False)
    
    def test_get_DEBUG_ProConfig(self):
        self.assertEqual(get_DEBUG_ProConfig(), False)
    
    def test_get_MAX_AGE_CORSConfig(self):
        self.assertEqual(get_MAX_AGE_CORSConfig(), 3600)
