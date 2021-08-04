"""

    *Be*   |べ|   |ベ|

  The _be_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Be"]

# [TODO] mechanism of extending


@dataclass
class Be(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3079"
    katakana = "\u30d9"
