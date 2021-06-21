import configparser


def load_config(path_config):
    """
    Loads a configuration from .ini file and returns as configparser
    """
    if path_config is None:
        raise FileNotFoundError(f"Could not find config at path: {str(path_config)}")

    config = configparser.ConfigParser()
    config.read(str(path_config))
    return config
