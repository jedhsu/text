from typing import Pattern

import markdown


class _BlockSyntax:
    _header_pattern: Pattern
    _page: Page
    _is_xml: bool


class _Parse_(_BlockSyntax):
    pass


class BlockSyntax:
    pass
