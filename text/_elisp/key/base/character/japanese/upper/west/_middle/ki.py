"""

    *Ki*   |き|   |キ|

  The _ki_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ki"]

# [TODO] mechanism of extending


@dataclass
class Ki(
    Gi,
    JapaneseGi,
):
    hiragana = "\u304d"
    katakana = "\u30ad"
