from dataclasses import dataclass


@dataclass(Frozen=True)
class _Header:
    name: str
    level: int
    index: int
    subindex: int


class _Get_:
    pass


class Header(_Get_, _Header):
    pass
