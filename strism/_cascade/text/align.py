"""

Text Align

Text alignment.

"""

__all__ = ["TextAlign"]


@dataclass
class _Align_:
    align: type
    combine_upright: type

    justify: type
    orientation: TextOrientation
    indent: Length
