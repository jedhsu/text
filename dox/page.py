from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Sequence

__all__ = ["Page"]


class Template(Enum):
    Title = "Title"
    Toc = "Toc"
    Page = "Page"

@dataclass(frozen=True)
class _Page:
    title: str
    part: str
    ordinal: int
    chapters: Sequence[Page]


class _Parse_(_Page):
    def parse(self) -> Page:
        pass

    def create_codetag(self, index: int, name: str, options: str) -> CodeTag:
        pass


class _Get_(_Page):
    def get_markdown_path(self) -> Path:
        raise NotImplemented

    def get_html_path(self) -> Path:
        raise NotImplemented

    def get_code_tags(self) -> CodeTag:
        raise NotImplemented


class _Page_:
    def is_chapter(self) -> bool:
        pass

    def is_part(self) -> bool:
        pass

    def abbreviate(self) -> str:
        pass


class _GetPage_(_Page):
    @staticmethod
    def get_chapter(title: str) -> Page:
        pass

    @staticmethod
    def get_number(title: str) -> Page:
        pass
    
    def get_template(self) -> Template:
        if title == "Title:
            return Template.Title

    @staticmethod
    def get_adjacent(page: Page, offset: int) -> Page:
        pass


class Page(Find):
    pass
