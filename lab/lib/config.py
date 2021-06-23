"""
Reusable code for configuration loading
"""

from configparser import ConfigParser
from pathlib import Path


def load_config(path_config: str) -> ConfigParser:
    """
    Loads a configuration from .ini file and returns as ConfigParser
    """
    # If config path was obtained from an environment variable, in case of that env variable not existing it will
    # fail silently returning None. In that case, Configparser does not refuse reading from None but simply
    # loads nothing, leading to unhelpful error messages further down the line when trying to access its contents.
    # Instead, better fail early:
    if path_config is None:
        raise ValueError(f"Please provide a valid filepath for config (received: {str(path_config)}).")

    if not Path(path_config).exists():
        raise FileNotFoundError(f"Could not find config at path: {str(path_config)}")

    config = ConfigParser()
    config.read(str(path_config))
    return config
