"""

    *Shi*   |し|   |シ|

  The _shi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Shi"]

# [TODO] mechanism of extending


@dataclass
class Shi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3057"
    katakana = "\u30b7"
