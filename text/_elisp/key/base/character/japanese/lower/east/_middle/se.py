"""

    *Se*   |せ|   |セ|

  The _se_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Se"]

# [TODO] mechanism of extending


@dataclass
class Se(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305b"
    katakana = "\u30bb"
