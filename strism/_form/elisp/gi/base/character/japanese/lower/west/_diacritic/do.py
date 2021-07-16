"""

    *Do*   |む|   |ム|

  The _ho_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Do"]

# [TODO] mechanism of extending


@dataclass
class Do(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307b"
    katakana = "\u30db"
