"""

    *Bu*   |ぶ|   |ブ|

  The _bu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Bu"]

# [TODO] mechanism of extending


@dataclass
class Bu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3076"
    katakana = "\u30d6"
