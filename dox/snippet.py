"""

Snippet of source code.

"""


@dataclass(frozen=True)
class Snippet:
    source_path: Path
    code_tag: CodeTag

    _location: Location

    _starting_line: int
    _ending_line: int
