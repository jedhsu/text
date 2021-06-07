from dataclasses import dataclass


class Px(int):
    def __init__(self, px: int):
        super(Px, self).__new__(int, px)


class Color(bytes):
    pass

class Font(str):
    def __init__(self, font: str):
        super(Font, self).__new__(str, font)

@dataclass
class Html:
    width: float = 1
    height: float = 1


@dataclass
class Body:
    pass


@dataclass
class Article:
    margin: int
    padding: int
    max_width: int


@dataclass
class Main:
    padding: int
    background: str
    border_radius

@dataclass
class H2:
    font: pass
