from dataclasses import dataclass
from typing import Sequence

from .rule import Rule


@dataclass(frozen=True)
class Grammar:
    keywords: Sequence[str]
    types: Sequence[str]
    rules: set[Rule]
