# Colorzz

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    app_bg: str = "#89b4fa"
    text_bg: str = "#7f849c"
    text_fg: str = "#cdd6f4"

    button_bg: str = "#7f849c"
    button_fg: str = "#cdd6f4"

    active_button_bg: str = "#232634"
    active_button_fg: str = "#11111b"


