"""

    *Mi*   |み|   |ミ|

  The _mi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Mi"]

# [TODO] mechanism of extending


@dataclass
class Mi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307f"
    katakana = "\u30df"
