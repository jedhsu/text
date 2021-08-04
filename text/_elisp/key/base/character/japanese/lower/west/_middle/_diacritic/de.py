"""

    *De*   |で|   |デ|

  The _de_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["De"]

# [TODO] mechanism of extending


@dataclass
class De(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3067"
    katakana = "\u30c7"
