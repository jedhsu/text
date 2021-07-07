from dataclasses import dataclass
from typing import Union


@dataclass
class FontFace(AtRule):
    line_gap_override: Annotated[
        bool, property
    ]  # [TODO] keep playing with this - but we want to clarify it's return. Time for Annotated

    range: property
    src: property
    size_adjust: property
    ascent_override: property


class FontFace(AtRule):
    @property
    def descent_override(self) -> Union[Normal, Percentage]:
        pass
