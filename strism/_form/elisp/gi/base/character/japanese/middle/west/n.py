"""

    *N*   |ん|   |ン|

  The _n_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["N"]

# [TODO] mechanism of extending


@dataclass
class N(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3093"
    katakana = "\u30f3"
