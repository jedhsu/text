"""

    *Te*   |て|   |テ|

  The _te_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Te"]

# [TODO] mechanism of extending


@dataclass
class Te(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3066"
    katakana = "\u30c6"
