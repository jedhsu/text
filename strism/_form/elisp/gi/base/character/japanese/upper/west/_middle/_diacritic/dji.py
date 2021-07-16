"""

    *Dji*   |は|   |ハ|

  The _dji_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Dji"]

# [TODO] mechanism of extending


@dataclass
class Dji(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306f"
    katakana = "\u30cf"
