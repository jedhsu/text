"""

    *Ka*   |か|   |カ|

  The _ka_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ka"]

# [TODO] mechanism of extending


@dataclass
class Ka(
    Gi,
    JapaneseGi,
):
    hiragana = "\u304b"
    katakana = "\u30ab"
