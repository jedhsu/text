"""

    *Hi*   |ひ|   |ヒ|

  The _hi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Hi"]

# [TODO] mechanism of extending


@dataclass
class Hi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3072"
    katakana = "\u30d2"
