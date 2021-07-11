from enum import Enum


class TerminalBackgroundMode(Enum):
    Light = "light"
    Dark = "dark"


class TerminalBackspaceErase(bool):
    def __init__(self, val: bool):
        super(TerminalBackspaceErase, self).__new__(
            bool,
            val,
        )


class TerminalParameters:
    pass
