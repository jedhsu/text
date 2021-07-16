"""

    *Ke*   |け|   |ケ|

  The _ke_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ke"]

# [TODO] mechanism of extending


@dataclass
class Ke(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3051"
    katakana = "\u30b1"
