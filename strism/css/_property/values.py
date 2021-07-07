"""

    *Values*

"""

from dataclasses import dataclass
from typing import Sequence

from .keyword import Keyword

__all__ = ["Values"]


@dataclass
class Values(
    tuple[Keyword],
):
    def __init__(
        self,
        keywords: Sequence[Keyword],
    ):
        super(Values, self).__new__(
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
        Values.create(
            "abc",
            "def",
        )
