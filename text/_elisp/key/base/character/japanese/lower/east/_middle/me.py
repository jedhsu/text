"""

    *Me*   |め|   |メ|

  The _me_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Me"]

# [TODO] mechanism of extending


@dataclass
class Me(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3081"
    katakana = "\u30e1"
