
class DevConfig:
    DEBUG = True

class BaseConfig():
    SECRET_KEY = "key"
    DEBUG = True
    TESTING = True

class DevConfig(BaseConfig):
    pass

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False

class CORSConfig:
    ORIGINS = ['http://example.com']
    METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 3600
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = True
    VARY_HEADER = True
