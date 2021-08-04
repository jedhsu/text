"""

    *Ya*   |や|   |ヤ|

  The _ya_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ya"]

# [TODO] mechanism of extending


@dataclass
class Ya(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3084"
    katakana = "\u30e4"
