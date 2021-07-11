"""

[SVG]

"""


class SvgElement:

    __metaclass__ = ABCMeta

    pass


# [TODO] think about Renderable trait


class Svg(Renderable, SvgElement):
    pass


class Symbol(SvgElement):
    pass


class Group(SvgElement):
    symbol = "g"
