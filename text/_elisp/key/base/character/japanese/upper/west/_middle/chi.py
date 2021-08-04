"""

    *Chi*   |ち|   |チ|

  The _chi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Chi"]

# [TODO] mechanism of extending


@dataclass
class Chi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3061"
    katakana = "\u30c1"
