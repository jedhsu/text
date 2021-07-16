"""

    *Tu*   |む|   |ム|

  The _tu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Tu"]

# [TODO] mechanism of extending


@dataclass
class Tu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3080"
    katakana = "\u30e0"
