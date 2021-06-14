from __future__ import annotations
from abc import ABCMeta
from dataclasses import dataclass
from typing import Literal, Optional, Sequence, Text


class Description(Sequence[Text], metaclass=ABCMeta):
    pass


class Items(Sequence[Text], metaclass=ABCMeta):
    pass


@dataclass
class Section(metaclass=ABCMeta):
    title: Text
    level: Literal[1, 2, 3, 4, 5, 6]

    description: Optional[Sequence[Text]]
    items: Optional[Sequence[Text]]
    sections: Optional[Sections]


class Sections(Sequence[Section], metaclass=ABCMeta):
    pass
