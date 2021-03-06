"""

    *Pa*   |ぱ|   |パ|

  The _pa_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Pa"]

# [TODO] mechanism of extending


@dataclass
class Pa(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3071"
    katakana = "\u30d1"
