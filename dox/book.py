from dataclasses import dataclass
from typing import MutableSequence, Optional

from .page import Page

__all__ = ["Book"]


@dataclass
class _Page:
    sections: dict[str, list[Page]]


class _GetPage_(_Page):
    def get_chapter(self, title: str) -> Optional[Page]:
        for page in self.sections.values():
            if page.title == title:
                return page

    @staticmethod
    def get_number(title: str) -> Page:
        pass

    @staticmethod
    def get_adjacent(page: Page, offset: int) -> Page:
        pass


class _Split_(_Page):
    def split_chapter(self, chapter: Page, tag: Optional[CodeTag]):
        pass

    def split_source(self):
        pass


class Book(_GetPage_):
    pass
