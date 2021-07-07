from dataclasses import dataclass


class Margin:
    block: property
    block_start: property
    block_end: property

    top: property
    right: property
    bottom: property
    left: property


class Scroll(Margin):
    behavior: type
    margin: type


# scroll-margin-inline
# scroll-margin-inline-end
# scroll-margin-inline-start


# scroll-padding
# scroll-padding-block
# scroll-padding-block-end
# scroll-padding-block-start


@dataclass
class PaddingInline:
    start: type
    end: type


@dataclass
class Padding:
    bottom: type
    left: type
    right: type
    top: type


@dataclass
class Snap:
    align: property
    stop: property
    type: property


@dataclass
class ScrollBar:
    color: type
    gutter: type
    width: type


@dataclass
class OverscrollBehavior:
    block: type
    inline: type

    x: type
    y: type
