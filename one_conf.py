import flask_cors import CORS
from configuration.configuration import CORSConfig

def set_debug(entrada):
    CORSConfig.BaseConfig.debug = entrada