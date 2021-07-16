"""

    *Ba*   |ば|   |バ|

  The _ba_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ba"]

# [TODO] mechanism of extending


@dataclass
class Ba(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3070"
    katakana = "\u30d0"
