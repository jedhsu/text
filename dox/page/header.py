from dataclasses import dataclass


@dataclass
class _Header:
    name: str
    level: int
    index: int
    subindex: int


class _Get_(_Header):
    def is_note(self):
        pass

    def is_warning(self):
        pass

    def is_todo(self):
        pass

    def is_special(self):
        pass


class Header(_Get_, _Header):
    pass
