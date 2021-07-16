"""

    *Ta*   |た|   |タ|

  The _ta_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ta"]

# [TODO] mechanism of extending


@dataclass
class Ta(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305f"
    katakana = "\u30bf"
