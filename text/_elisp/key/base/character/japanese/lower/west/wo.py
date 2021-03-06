"""

    *Wo*   |を|   |ヲ|

  The _wo_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Wo"]

# [TODO] mechanism of extending


@dataclass
class Wo(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3092"
    katakana = "\u30f2"
