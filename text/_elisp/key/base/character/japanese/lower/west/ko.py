"""

    *Ko*   |こ|   |コ|

  The _ko_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ko"]

# [TODO] mechanism of extending


@dataclass
class Ko(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3053"
    katakana = "\u30b3"
