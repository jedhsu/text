"""

    *Cascade: Values*

  The set of valid values that defines a property.

"""

from dataclasses import dataclass
from typing import Sequence

from ..keyword import Keyword

__all__ = ["CascadeValues"]


@dataclass
class CascadeValues(
    tuple[Keyword],
):
    def __init__(
        self,
        keywords: Sequence[Keyword],
    ):
        super(CascadeValues, self).__new__(
            tuple,
            keywords,
        )

    @classmethod
    def create(
        cls,
        *keyword: str,
    ):
        keywords = [*keyword]
        return cls([Keyword(kw) for kw in keywords])


class Test:
    @staticmethod
    def create():
        CascadeValues.create(
            "abc",
            "def",
        )
