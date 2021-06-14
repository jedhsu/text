from dataclasses import dataclass

from ..measure import Length

__all_ = ["Text"]


class TextTransform:
    """
    Transform case.

    """

    # keyword = "text-transform"

    Capitalize = "capitalize"
    Uppercase = "uppercase"
    Lowercase = "lowercase"
    None_ = "none"  # disable


class TextDecoration:
    Underline = "underline"
    Overline = "overline"
    LineThrough = "line-through"
    Blink = "blink"
    None_ = "none"


class DecorationStyle:
    Solid = "solid"
    Double = "double"
    Dotted = "dotted"
    Dashed = "dashed"
    Wavy = "wavy"


@dataclass
class _Transform_:
    overflow: property
    rendering: property
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
class _Align_:
    align: type
    combine_upright: type

    justify: type
    orientation: type

    indent: Length


class HorizontalAlign:
    """
    (Text Align)

    """

    Start = "start"
    End = "end"

    Left = "left"
    Right = "right"
    Center = "center"
    Justify = "justify"


class VerticalAlign:
    """
    vertical-align

    """

    Baseline = "baseline"
    Subscript = "sub"
    Superscript = "super"

    Top = "top"
    Middle = "middle"
    Bottom = "bottom"

    TextTop = "text-top"
    TextBottom = "text-bottom"


class TextIndent(Length, Percentage):
    pass


class TextAlignLast(TextAlign):
    """
    Text alignment of last line.

    """

    pass


class LetterSpacingKeyword:
    Normal = "normal"


class LetterSpacing(LetterSpacingKeyword, Length):
    pass


class Hyphens:
    Auto = "auto"
    Manual = "manual"
    None_ = "none"


class HangingPunctuation:
    """
    Specifies whether punctuatino should hang at start or end of a line of text.

    """

    None_ = "none"

    First = "first"
    Last = "last"
    ForceEnd = "force-end"
    AllowEnd = "allow-end"

    # [TODO] combinations


@dataclass
class _Emphasis_:
    emphasis: type
    emphasis_color: type
    emphasis_position: type
    emphasis_style: type


@dataclass
class Text(
    _Emphasis_,
    _Align_,
    _Decorate_,
    _Underline_,
    _Transform_,
):
    pass


class Whitespace:
    """
    Whitespace colllapsing.

    """

    Normal = "normal"
    Nowrap = "nowrap"
    PreLine = "pre-line"
