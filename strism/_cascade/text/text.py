from dataclasses import dataclass

from ..measure import Length

__all__ = ["Text"]


@dataclass
class _Transform_:
    overflow: property
    rendering: TextRendering
    shadow: property
    size_adjust: property
    transform: property


@dataclass
class _Underline_:
    underline_offset: property
    underline_position: property


@dataclass
class _Decorate_:
    decoration_color: type
    decoration_line: type
    decoration_skip: type
    decoration_skip_ink: type
    decoration_thickness: type


@dataclass
class Text(
    _Emphasis_,
    _Align_,
    _Decorate_,
    _Underline_,
    _Transform_,
):
    pass
