"""

    *No*   |の|   |ノ|

  The _no_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["No"]

# [TODO] mechanism of extending


@dataclass
class No(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306e"
    katakana = "\u30ce"
