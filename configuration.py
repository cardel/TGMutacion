class BaseConfig():
    SECRET_KEY = "key"
    DEBUG = True
    TESTING = True

class DevConfig(BaseConfig):
    pass

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False