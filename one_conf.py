from flask_cors import CORS
from configuration.configuration import CORSConfig

def set_debug():
    return CORSConfig.BaseConfig.debug