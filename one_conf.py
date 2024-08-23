from configuration.configuration import DevConfig, BaseConfig, ProConfig, CORSConfig

def get_DEBUG_DevConfig():
    return DevConfig.DEBUG

def get_DEBUG_BaseConfig():
    return BaseConfig.DEBUG

def get_DEBUG_ProConfig():
    return ProConfig.DEBUG

def get_MAX_AGE_CORSConfig():
    return CORSConfig.MAX_AGE
