from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence


class Kind(Enum):
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
    parent: Location
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


Html = str


class _Convert_(_Location):
    def into_string(self) -> str:
        pass

    def into_html(
        self,
        preceding: Location,
        removed: Sequence[str],
    ) -> Html:
        if self.kind == Kind.New:
            return "create new file"
        elif self.kind == Kind.Top:
            return "add to top of file"
        elif self.kind == Kind.Class and self.parent.kind == Kind.Class:
            return f"nest inside class <em>{preceding.name}</em>{preceding.signature})"

    def into_xml(self) -> str:
        pass


class Location(
    _Convert_,
    _Hashable_,
    Kind,
    _Location,
):
    pass
