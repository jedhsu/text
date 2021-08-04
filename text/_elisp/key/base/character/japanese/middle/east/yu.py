"""

    *Yu*   |ゆ|   |ユ|

  The _yu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Yu"]

# [TODO] mechanism of extending


@dataclass
class Yu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3086"
    katakana = "\u30e6"
