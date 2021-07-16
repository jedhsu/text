"""

    *Po*   |ぽ|   |ポ|

  The _po_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Po"]

# [TODO] mechanism of extending


@dataclass
class Po(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307d"
    katakana = "\u30dd"
