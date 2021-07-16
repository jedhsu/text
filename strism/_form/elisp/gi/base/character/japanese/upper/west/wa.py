"""

    *Wa*   |わ|   |ワ|

  The _wa_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Wa"]

# [TODO] mechanism of extending


@dataclass
class Wa(
    Gi,
    JapaneseGi,
):
    hiragana = "\u308f"
    katakana = "\u30ef"
