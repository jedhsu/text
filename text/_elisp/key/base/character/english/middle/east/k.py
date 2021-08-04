"""

    *H*   h

  The _h_ gi of the English language.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import EnglishGi

__all__ = ["H"]


@dataclass
class H(
    Gi,
    EnglishGi,
):
    symbol = "h"
