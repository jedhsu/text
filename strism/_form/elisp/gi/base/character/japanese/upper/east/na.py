"""

    *Na*   |な|   |ナ|

  The _na_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Na"]

# [TODO] mechanism of extending


@dataclass
class Na(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306a"
    katakana = "\u30ca"
