"""

    *J*   j

  The _j_ gi of the English language.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import EnglishGi

__all__ = ["J"]


@dataclass
class J(
    Gi,
    EnglishGi,
):
    symbol = "j"
