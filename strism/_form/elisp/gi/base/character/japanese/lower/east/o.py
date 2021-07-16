"""

    *O*    |お|   |オ|

  The _o_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["O"]

# [TODO] mechanism of extending


@dataclass
class O(
    Gi,
    JapaneseGi,
):
    hiragana = "\u304a"
    katakana = "\u30aa"
