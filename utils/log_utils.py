"""
    Load the logger for the current module
"""
import os
import json
import logging.config


def load_logger(default_path='log-config.json', default_level=logging.INFO):
    """
    Sets up the logger
    :param default_path: El path por defecto del archivo de configuracion
    :param default_level:  El nivel de log por defecto
    :return:
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.DictConfigurator(config)
    else:
        logging.basicConfig(level=default_level)
