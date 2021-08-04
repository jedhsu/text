"""

    *Ru*   |る|   |ル|

  The _ru_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ru"]

# [TODO] mechanism of extending


@dataclass
class Ru(
    Gi,
    JapaneseGi,
):
    hiragana = "\u308b"
    katakana = "\u30eb"
