"""

    *Zo*   |せ|   |セ|

  The _zo_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Zo"]

# [TODO] mechanism of extending


@dataclass
class Zo(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305b"
    katakana = "\u30bb"
