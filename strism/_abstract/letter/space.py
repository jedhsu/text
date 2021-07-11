"""

    *Abstract Letter-Space*

  A letter space defines the space of letters.

"""

from dataclasses import dataclass

from ._letter import AbstractLetter

__all__ = ["AbstractLetterSpace"]


@dataclass
class AbstractLetterSpace(
    set[AbstractLetter],
):
    ident: str

    def __init__(
        self,
        ident: str,
        space: set[AbstractLetter],
    ):
        self.ident = ident
        super(AbstractLetterSpace, self).__new__(
            set,
            space,
        )

    @classmethod
    def create(
        cls,
        ident: str,
        space: set[str],
    ):
        return cls(
            ident,
            {AbstractLetter(lt) for lt in space},
        )
