from dataclasses import dataclass
from typing import Sequence


@dataclass
class Descriptor:
    ident: str
    value: Sequence
    important: bool
