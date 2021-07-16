"""

    *Gu*   |ぐ|   |グ|

  The _gu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Gu"]

# [TODO] mechanism of extending


@dataclass
class Gu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3050"
    katakana = "\u30b0"
