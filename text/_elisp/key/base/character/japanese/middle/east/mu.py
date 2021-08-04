"""

    *Mu*   |む|   |ム|

  The _mu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Mu"]

# [TODO] mechanism of extending


@dataclass
class Mu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3080"
    katakana = "\u30e0"
