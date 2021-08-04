"""

    *Bi*   |び|   |ビ|

  The _bi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Bi"]

# [TODO] mechanism of extending


@dataclass
class Bi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3073"
    katakana = "\u30d3"
