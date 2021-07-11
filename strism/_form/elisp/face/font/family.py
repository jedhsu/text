"""

    Font Family

  The font family.

"""

from dataclasses import dataclass

__all__ = ["FontFamily"]


@dataclass
class FontFamily:
    name: NameIdent
    foundry: NameIdent
