from dataclasses import dataclass


@dataclass
class _CodeTag:
    name: str
    chapter: Page

    _index: int

    before_count: int
    after_count: int

    show_location: bool


class _Order_:
    pass


class _Create:
    pass


class _Convert_:
    def into_string(self):
        pass


class CodeTag(_Order_):
    pass
