"""

    *H*   h

  The _h_ gi of the English language.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import EnglishGi

from strism._form.elisp.gi.base.character._strismic import MiddleEast0

__all__ = ["H"]


@dataclass
class H(
    Gi,
    EnglishGi,
):
    symbol = "h"
