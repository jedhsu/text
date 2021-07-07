"""

    *Property-Declare*

  Declare a property.

"""

from ._operator import PropertyOperator


class PropertyDeclare(
    PropertyOperator,
):
    pass


"""

    *Declaration-Block*

"""

from typing import Sequence
from dataclasses import dataclass

__all__ = ["DeclarationBlock"]

from .declaration import Declaration


@dataclass
class DeclarationBlock:
    INDENT_LENGTH = 4

    declarations: Sequence[Declaration]

    @classmethod
    def indent(cls, line: str) -> str:
        """
        Indents a line of text.

        """
        return " " * cls.INDENT_LENGTH + line

    def into_css(self) -> str:
        declarations = [decl.into_css() for decl in self.declarations]
        declarations = [self.indent(decl) + ";" for decl in declarations]
        declarations = ["{"] + declarations + ["}"]
        declarations = "\n".join(declarations)
        return declarations
