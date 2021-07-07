"""

    *Abstract Character-Space*

  A character space defines the space of characters.

"""

from dataclasses import dataclass

from ._character import AbstractCharacter

__all__ = ["AbstractCharacterSpace"]


@dataclass
class AbstractCharacterSpace(
    set[AbstractCharacter],
):
    ident: str

    def __init__(
        self,
        ident: str,
        space: set[AbstractCharacter],
    ):
        self.ident = ident
        super(AbstractCharacterSpace, self).__init__(
            space,
        )
