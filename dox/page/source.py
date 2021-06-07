from dataclasses import dataclass
import re
from typing import Mapping, Sequence

from ..codetag import CodeTag
from .header import Header


class Patterns:
    code = r"^\^code ([-a-z0-9]+)( \(([^)]+)\))?$"
    header = r"^(#{1,3}) "
    before = r"(\d+) before"
    after = r"(\d+) after"


@dataclass
class PageSource:
    lines: Sequence[str]
    headers: Mapping[str, Header]
    codetags: Mapping[str, CodeTag]

class _Parse_(PageSource):

    headers: dict[str, Header] = {}
    codetags: dict[str, CodeTag] = {}

    header_index = 0
    subheader_index = 0
    

        with open(self.path, "rb") as fio:
            lines = fio.readlines()

    def parse(self):
        for line in lines:
            match = re.match(Patterns.code, line)
            if match:
                codetag = CodeTag(
