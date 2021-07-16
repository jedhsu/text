"""

    *Ra*   |ら|   |ラ|

  The _ra_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ra"]

# [TODO] mechanism of extending


@dataclass
class Ra(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3089"
    katakana = "\u30e9"
