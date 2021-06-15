"""

Flexible box layout.

"""

from dataclasses import dataclass

from ...base import Property, ShorthandProperty


class GridDisplay:
    """
    Display options for Flex.

    """

    Flex = "flex"
    InlineFlex = "inline-flex"


class FlexDirection(Property):
    # x-direction
    Row = "row"
    RowReverse = "row-reverse"

    # y-direction
    Column = "column"
    ColumnReverse = "column-reverse"


class FlexContainer:
    """
    Box generated by an element with a computed display of flex.

    """

    pass


class FlexItem:
    pass


class FlexAxis:
    pass


class MainAxis(FlexAxis):
    pass


class CrossAxis(FlexAxis):
    pass


@dataclass
class FlexibleBoxLayout(Module):
    flex: ShorthandProperty

    flex_direction: FlexDirection

    flex_basis: FlexBasis
    flex_grow: FlexGrow
    flex_shrink: FlexShrink

    order: Property


class FlexBasis(Length):
    pass


class FlexGrow(Length):
    pass


class FlexShrink(Length):
    pass


class FlexWrap(Property):
    """
    Orientation.

    """

    NoWrap = "nowrap"
    Wrap = "wrap"
    WrapReverse = "wrap-reverse"


class FlexFlow(ShorthandProperty):
    """
    Shorthand for flex direction and wrap.

    """

    pass


pass


class JustifyContent:
    FlexStart = "flex-start"
    FlexEnd = "flex-end"

    Center = "center"

    SpaceAround = "space-around"
    SpaceBetween = "space-between"
    SpaceEvenly = "space-evenly"
