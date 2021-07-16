"""

    *Gi*   |は|   |ハ|

  The _gi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Gi"]

# [TODO] mechanism of extending


@dataclass
class Gi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306f"
    katakana = "\u30cf"
