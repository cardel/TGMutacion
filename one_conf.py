from configuration.configuration import BaseConfig, ProConfig, CORSConfig


def set_TESTING_Pro():
    if ProConfig.TESTING:
        ProConfig.TESTING = True
    return ProConfig.TESTING

