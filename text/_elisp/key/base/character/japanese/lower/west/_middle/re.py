"""

    *Re*   |れ|   |レ|

  The _re_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Re"]

# [TODO] mechanism of extending


@dataclass
class Re(
    Gi,
    JapaneseGi,
):
    hiragana = "\u308c"
    katakana = "\u30ec"
