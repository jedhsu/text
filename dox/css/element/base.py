from abc import ABCMeta


class Element:
    pass


class ReplacedElement(Element):
    pass


class NonReplacedElement(Element):
    pass


class BlockElement(Element):
    pass


class InlineElement(Element):
    pass


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
