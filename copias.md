# one_conf.py copies
def get_DEBUG_DevConfig():
    return DevConfig.DEBUG

def get_DEBUG_BaseConfig():
    return BaseConfig.DEBUG

def get_DEBUG_ProConfig():
    return ProConfig.DEBUG

def get_MAX_AGE_CORSConfig():
    return CORSConfig.MAX_AGE


# test_security.py copies
from one_conf import get_DEBUG_DevConfig, get_DEBUG_BaseConfig, get_DEBUG_ProConfig, get_MAX_AGE_CORSConfig

    def test_get_DEBUG_DevConfig(self):
        self.assertEqual(get_DEBUG_DevConfig(), True)
    
    def test_get_DEBUG_BaseConfig(self):
        self.assertNotEqual(get_DEBUG_BaseConfig(), False)
    
    def test_get_DEBUG_ProConfig(self):
        self.assertEqual(get_DEBUG_ProConfig(), False)
    
    def test_get_MAX_AGE_CORSConfig(self):
        self.assertEqual(get_MAX_AGE_CORSConfig(), 3600)

