"""

    *Nu*   |ぬ|   |ヌ|

  The _nu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Nu"]

# [TODO] mechanism of extending


@dataclass
class Nu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u306c"
    katakana = "\u30cc"
