"""
Reusable code for configuration loading
"""

import configparser


def load_config(path_config):
    """
    Loads a configuration from .ini file and returns as configparser
    """
    # If config path was obtained from environment variable, in case of the env variable not existing, it will
    # fail silently returning None. In that case, Configparser does not refuse reading from None but simply
    # loads nothing. Instead, better fail early:
    if path_config is None:
        raise FileNotFoundError(f"Could not find config at path: {str(path_config)}")

    config = configparser.ConfigParser()
    config.read(str(path_config))
    return config
