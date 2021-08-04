"""

    *Fu*   |ふ|   |フ|

  The _fu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Fu"]

# [TODO] mechanism of extending


@dataclass
class Fu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3075"
    katakana = "\u30d5"
