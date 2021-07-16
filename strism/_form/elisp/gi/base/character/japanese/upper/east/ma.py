"""

    *Ma*   |ま|   |マ|

  The _ma_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ma"]

# [TODO] mechanism of extending


@dataclass
class Ma(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307e"
    katakana = "\u30de"
