"""

Snippet of source code.

"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

from .codetag import CodeTag
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


class _Get_(_Snippet):
    pass


class _Update_(_Snippet):
    def add_line(
        self,
        index: int,
        line: SourceLine,
    ):
        pass


class _Get_(_Snippet):
    def get_location_html_lines(self) -> Sequence[str]:
        pass
