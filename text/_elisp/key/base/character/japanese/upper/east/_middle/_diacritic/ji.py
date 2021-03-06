"""

    *Ji*   |じ|   |ジ|

  The _ji_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ji"]

# [TODO] mechanism of extending


@dataclass
class Ji(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3058"
    katakana = "\u30b8"
