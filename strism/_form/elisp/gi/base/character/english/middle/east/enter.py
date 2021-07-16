"""

    *Enter*   h

  The _enter_ gi of the English language.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import EnglishGi

__all__ = ["Enter"]


@dataclass
class Enter(
    Gi,
    EnglishGi,
):
    symbol = "Enter"
