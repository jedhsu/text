"""

    *Mo*   |も|   |モ|

  The _mo_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Mo"]

# [TODO] mechanism of extending


@dataclass
class Mo(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3082"
    katakana = "\u30e2"
