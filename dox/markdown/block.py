from dataclasses import dataclass
from typing import Pattern

import markdown


@dataclass
class _BlockSyntax:
    _header_pattern: Pattern
    _page: Page
    _is_xml: bool


class _Parse_(_BlockSyntax):
    def parse(self):
        header = Element(f"h{header.level}", [UnparsedContent(header.name)])
        number = ""

        if not header._is_special():
            # number = f"{self._page.numberstring}&#8202;.&#8202;{header.name})])
            pass


class BlockSyntax:
    pass
