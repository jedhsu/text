"""

    *Pu*   |ぷ|   |プ|

  The _pu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Pu"]

# [TODO] mechanism of extending


@dataclass
class Pu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3077"
    katakana = "\u30d7"
