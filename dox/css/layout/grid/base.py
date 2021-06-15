# [TODO] feature query

from typing import Generic, Literal, TypeVar


class GridContainer:
    pass


# [TODO] need these types
T = TypeVar("T", Literal["Auto"], CustomIdent, int, CustomIdentInt, Span)


class GridLine(Generic[T]):
    """
    Boundary lines.

    """

    pass


class GridTrack:
    pass


class GridCell:
    """
    A single space on the grid.

    """

    pass


class GridArea:
    """
    A rectangular area on the grid made up of one or more grid cells.

    """

    pass


class GridAxis:
    pass
