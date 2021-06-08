"""

Code syntax.

"""

import re


class HighlightCodeBlockSyntax:
    _codefence_pattern = re.compile(r"^(\s*)```(.*)$")

    is_xml: bool


class CodeTagBlockSyntax:
    pass
