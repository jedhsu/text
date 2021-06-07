"""

Snippet of source code.

"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

from .codetag import CodeTag
from .html import Html
from .location import Location


@dataclass
class _Snippet:
    source_path: Path
    code_tag: CodeTag

    _location: Location

    _starting_line: int
    _ending_line: int

    _preceding_location: Optional[Location]
    _added_comma: Optional[str]

    added: list[str]
    removed: list[str]

    context_before: list[str]
    context_after: list[str]


class _Update_(_Snippet):
    def add_line(
        self,
        index: int,
        line: SourceLine,
    ):
        if not self:
            self._location = line.location
            self._starting_line = index
        self.added.append(line.text)

    def remove_line(
        self,
        index: int,
        line: SourceLine,
    ):
        self.removed.add(line.text)
        self._ending_line = index


class _Get_(_Snippet):
    def get_location_html_lines(self) -> Sequence[str]:
        result = [Html(self.source_path).wrap("em")]


class _Get_(_Snippet):
    def get_location_html_lines(self) -> Sequence[str]:
        pass
