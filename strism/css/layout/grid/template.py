from ...measure import Length


class GridLengthKeyword:
    Auto = "auto"


class GridLength(Length, GridLengthKeyword):
    pass


class GridAxis:
    """
    Sequence of grid length

    """


class GridTemplate:
    template_areas: type

    rows: GridAxis
    columns: GridAxis


class GridAxisGap(GridLength):
    """
    Combine with grid axis? which architecture do u like?

    """

    pass
