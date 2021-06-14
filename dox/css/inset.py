from dataclasses import dataclass
from typing import Callable


@dataclass
class Inset:
    inset: property  # [TODO] remember this is a shape

    inset_: Callable

    inset_block: property
    inset_block_start: property
    inset_block_end: property

    inset_inline: property
    inset_inline_start: property
    inset_inline_end: property
