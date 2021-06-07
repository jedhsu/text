from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Sequence


class Kind:
    New = "New"
    Top = "Top"
    Class = "Class"
    File = "File"
    Constructor = "Constructor"
    Function = "Function"
    Method = "Method"


class _Set_:
    name: Optional[str]

    def set_name(self, val: str):
        assert self.name is None
        self.name = val


@dataclass
class _Location(_Set_):
    parent: Optional[Location]
    kind: Kind
    name: Optional[str]
    signature: str
    is_func_declaration: bool


class _Hashable_(_Location):
    def __hash__(self):
        pass


class _Get_(_Location):
    def is_file(self) -> bool:
        return self.kind == Kind.File

    def is_function(self) -> bool:
        return self.kind in [
            Kind.Constructor,
            Kind.Function,
            Kind.Method,
        ]

    def depth(self) -> int:
        pass
        # current = self
        # result = 0
        # while current is not None:
        #     result += 1
        #     current = current.parent
        # return result


Html = str


class _Convert_(_Get_, _Location):
    def into_string(self) -> str:
        result = f"{repr(self.kind)} {repr(self.name)}"

        if self.signature:
            result += repr(self.signature)

        if self.parent:
            # [TODO] wat is this oeprator
            pass

        return result

    def into_html(
        self,
        preceding: Location,
        removed: Sequence[str],
    ) -> Optional[Html]:
        if self.kind == Kind.New:
            return "create new file"

        elif self.kind == Kind.Top:
            return "add to top of file"

        elif self.kind == Kind.Class and self.parent.kind == Kind.Class:
            return f"nest inside class <em>{preceding.name}</em>{preceding.signature})"

        elif self.is_function() and self == preceding:
            if self.name == "resolve" and self.signature == "Expr expr":
                return f"add after <em>{preceding.name}</em>({preceding.signature})"
            else:
                return f"in <em>{self.name}</em>()"

        elif self.is_function() and removed:
            return f"{self.kind} <em>{self.name}</em>"

        elif self.parent == preceding and not preceding.is_file():
            return f"in {preceding.kind} <em>${preceding.name}</em>"

        elif self.parent == self and not self.is_file():
            return f"in {self.kind} <em>{self.name}</em>"

        elif preceding.is_function():
            return f"add after <em>{preceding.name}</em>()"

        elif preceding.is_file():
            return f"add after {preceding.kind} <em>{preceding.name}</em>"

        else:
            return None

    def into_xml(self) -> str:
        if self.kind == "New":
            return "create new file"

        elif self.kind == "Top":
            return "add to top of file"

        elif self.kind == "Class" and self.parent.kind == "Class":
            return (
                f"nest inside class <location-type>{self.parent.name}</location-type>"
            )


class Location(
    _Convert_,
    _Hashable_,
    Kind,
    _Location,
):
    pass
