from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

from .page import Page

# [TODO] generalize from code tag adn have a math tag


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


class _Create_:
    @staticmethod
    def from_page(page: Page, index: int, name: str, options: Sequence[str]):
        show_location = True
        before_count = 0
        after_count = 0

        if options:
            for option in options:
                if option == "no location":
                    show_location = False
                    continue

                    raise ValueError("Unknown code option.")


class _Get_(_CodeTag):
    def directory(self) -> str:
        return f"00{self._index}-{self.name}"


class _Convert_(_CodeTag):
    def __cmp__(self, tag: CodeTag):
        if self.chapter.ordinal != tag.chapter.ordinal:
            return self.chapter.ordinal.__cmp__(tag.chapter.ordinal)

    def into_string(self) -> str:
        return f"Tag({self.chapter.ordinal}|{self._index}: {self.chapter} {self.name}"


class CodeTag(
    _Order_,
    _Convert_,
    _Create_,
    _Order_,
    _CodeTag,
):
    pass
