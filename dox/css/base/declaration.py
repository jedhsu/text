from dataclasses import dataclass
from typing import Sequence, Union


@dataclass
class Declaration:
    property: Property
    value: Union[str, int, float, bool]

    def into_css(self) -> str:
        return f"{self.property} : {self.value}"


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
