"""

    *Go*   |ご|   |ゴ|

  The _go_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Go"]

# [TODO] mechanism of extending


@dataclass
class Go(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3054"
    katakana = "\u30b4"
