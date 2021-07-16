"""

    *He*   |ほ|   |ヘ|

  The _he_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["He"]

# [TODO] mechanism of extending


@dataclass
class He(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307b"
    katakana = "\u30d8"
