"""

    *Declaration*

"""

from dataclasses import dataclass
from typing import Union

from .property import Property

__all__ = ["Declaration"]


@dataclass
class Declaration:
    property: Property
    value: Union[str, int, float, bool]

    def into_css(self) -> str:
        return f"{self.property} : {self.value}"
