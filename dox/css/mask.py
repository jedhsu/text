from dataclasses import dataclass


class MaskMode:
    Alpha = "alpha"
    Luminance = "luminance"
    MatchSource = "match-source"

    # [TODO] finish


class MaskComposite:
    Add = "add"
    Subtract = "subtract"
    Intersect = "intersect"
    Exclude = "exclude"


class MaskOrigin:
    ContentBox = "content-box"
    PaddingBox = "padding-box"
    BorderBox = "border-box"
    MarginBox = "margin-box"

    FillBox = "fill-box"
    StrokeBox = "stroke-box"
    ViewBox = "view-box"

    # [TODO] finish


@dataclass
class MaskBorder:
    border: type
    mode: type
    outset: type
    repeat: type
    slice: type
    source: type
    width: type


@dataclass
class Mask:
    mode: MaskMode
    composite: MaskComposite

    mask: type
    border: MaskBorder
    clip: type
    image: type
    origin: type
    position: type
    repeat: type
    size: type
    type: type
