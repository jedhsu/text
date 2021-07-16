"""

    *Su*   |す|   |ス|

  The _su_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Su"]

# [TODO] mechanism of extending


@dataclass
class Su(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3059"
    katakana = "\u30b9"
