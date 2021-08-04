from dataclasses import dataclass
from typing import Callable

"""

Can define constructors using array syntax.

"""


class GridDisplay:
    """
    Display options for Grid.

    """

    Grid = "grid"
    InlineGrid = "inline-grid"
    Subgrid = "subgrid"


class GridAutoFlow:
    Row = "row"
    Column = "column"
    Dense = "dense"


@dataclass
class Grid:
    area: type

    auto_flow: GridAutoFlow
    auto_columns: type
    auto_rows: type

    column: type
    column_end: type
    column_start: type

    row: type
    row_end: type
    row_start: type


minmax_: Callable
repeat_: Callable
fit_content_: Callable

masonry_auto_flow: property
