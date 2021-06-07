from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, Sequence

__all__ = ["Page"]


class Template:
    Title = "Title"
    Toc = "Toc"
    Page = "Page"


@dataclass
class _Page:
    title: str
    numstr: str

    ordinal: int
    chapters: Sequence[Page]

    part: Optional[Page]


class _Parse_(_Page):
    def parse(self) -> Page:
        pass

    def create_codetag(self, index: int, name: str, options: str) -> CodeTag:
        pass


class _Path_(_Page):
    def markdown_path(self) -> Path:
        return Path("book", f"{self.title}.md")

    def html_path(self) -> Path:
        return Path("site", f"{self.title}.html")

class _Get_(_Page):
    def is_chapter(self) -> bool:
        return self.part is None
    
    def is_part(self) -> bool:
        return self.part is not None
    
    def language(self) -> str:
        pass
    
    def abbrev(self) -> str:
        pass

    def code_tags(self) -> CodeTag:
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
