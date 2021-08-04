"""

    *Ne*   |ね|   |ネ|

  The _ne_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ne"]

# [TODO] mechanism of extending


@dataclass
class Ne(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306d"
    katakana = "\u30cd"
