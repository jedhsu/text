"""

    *Prefix-Key*

  A prefix key is a key whose binding is a keymap.

"""

from typing import Sequence
from dataclasses import dataclass

from .event import KeyEvent
from ._key import Key

__all__ = [
    "PrefixKey",
]


@dataclass
class PrefixKey(
    Key,
):
    def __init__(
        self,
        events: Sequence[KeyEvent],
    ):
        super(PrefixKey, self).__init__(
            events,
        )
