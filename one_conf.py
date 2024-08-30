from configuration.configuration import BaseConfig, ProConfig, CORSConfig

def set_DEBUG_Base():
    if not BaseConfig.DEBUG:
        BaseConfig.DEBUG = False
    return BaseConfig.DEBUG

def set_TESTING_Pro():
    if ProConfig.TESTING:
        ProConfig.TESTING = True
    return ProConfig.TESTING

def set_SUPP_CREDENTIALS():
    if not CORSConfig.SUPPORTS_CREDENTIALS:
        CORSConfig.SUPPORTS_CREDENTIALS = False
    return CORSConfig.SUPPORTS_CREDENTIALS

