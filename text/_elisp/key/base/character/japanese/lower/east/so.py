"""

    *So*   |そ|   |ソ|

  The _so_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["So"]

# [TODO] mechanism of extending


@dataclass
class So(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305d"
    katakana = "\u30bd"
