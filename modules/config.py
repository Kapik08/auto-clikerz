# config.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    # Settingzz
    window_x: str = '400'
    window_y: str = '500'
    windowSize: str = ""  # Initialize as empty, will be filled next

    button_fontFamily: str = 'JetBrains Mono'
    button_fontSize: int = 10

    fontSize: int = 10
    buttonWidth: int = 10
    uniHeight: int = 40

    def __post_init__(self):
        # This bypasses the frozen restriction to calculate windowSize
        object.__setattr__(self, 'windowSize', f"{self.window_x}x{self.window_y}")
