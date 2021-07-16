"""

    *Sa*   |さ|   |サ|

  The _sa_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Sa"]

# [TODO] mechanism of extending


@dataclass
class Sa(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3055"
    katakana = "\u30b5"
