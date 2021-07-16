"""

    *Ku*   |く|   |ク|

  The _ku_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ku"]

# [TODO] mechanism of extending


@dataclass
class Ku(
    Gi,
    JapaneseGi,
):
    hiragana = "\u304f"
    katakana = "\u30af"
