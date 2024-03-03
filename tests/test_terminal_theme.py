import os
import importlib
from rich.global_config import load_global_config
import rich.terminal_theme


def test_global_config():
    os.environ["RICH_THEME_FILE"] = "tests/theme_config_test.toml"
    terminal_theme = importlib.reload(rich.terminal_theme)

    theme = terminal_theme.DEFAULT_TERMINAL_THEME

    assert theme.background_color == (1, 2, 3) and theme.foreground_color == (4, 5, 6)
