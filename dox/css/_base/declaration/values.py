"""

Values

"""

from dataclasses import dataclass

__all__ = ["Values"]
from ..keyword import Keyword


@dataclass
class Values(
    tuple[Keyword],
):
    def __init__(self, *keywords: Keyword):
        super(Values, self).__new__(
            tuple,
            [*keywords],
        )
