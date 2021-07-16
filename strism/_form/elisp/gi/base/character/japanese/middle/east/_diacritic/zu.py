"""

    *Zu*   |ず|   |ズ|

  The _zu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Zu"]

# [TODO] mechanism of extending


@dataclass
class Zu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u305a"
    katakana = "\u30ba"
