"""

    *Za*   |い|   |イ|

  The _za_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Za"]

# [TODO] mechanism of extending


@dataclass
class Za(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3044"
    katakana = "\u30a4"
