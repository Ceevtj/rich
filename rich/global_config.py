from typing import Optional, Any, Dict
import os

import toml


DEFAULT_CONFIG_PATH = "/rich/config.toml"


def load_global_config() -> Optional[Dict[str, Any]]:
    """
    Load the global config file.
    """
    config_file = None
    if "RICH_NO_GLOBAL_CONFIG" in os.environ:
        return None
    if "RICH_THEME_FILE" in os.environ:
        config_file = os.environ["RICH_THEME_FILE"]
    elif "XDG_CONFIG_HOME" in os.environ:
        config_file = os.environ["XDG_CONFIG_HOME"] + DEFAULT_CONFIG_PATH

    if config_file is None or not os.path.isfile(config_file):
        return None
    return toml.load(config_file)
