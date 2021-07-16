"""

    *E*   |え|   |エ|

  The _e_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["E"]

# [TODO] mechanism of extending


@dataclass
class E(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3048"
    katakana = "\u30a8"
