"""

    *Ze*   |せ|   |セ|

  The _ze_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ze"]

# [TODO] mechanism of extending


@dataclass
class Ze(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305b"
    katakana = "\u30bb"
