"""

    *Ni*   |に|   |ニ|

  The _hi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ni"]

# [TODO] mechanism of extending


@dataclass
class Ni(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306b"
    katakana = "\u30cb"
