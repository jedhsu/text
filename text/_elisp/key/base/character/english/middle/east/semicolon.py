"""

    *Semicolon*   ;

  The _;_ gi of the English language.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import EnglishGi

__all__ = ["Semicolon"]


@dataclass
class Semicolon(
    Gi,
    EnglishGi,
):
    symbol = ";"
