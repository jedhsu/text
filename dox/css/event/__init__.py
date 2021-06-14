"""

User events.

"""

touch_action: property  # touch screen


class PointerEvents:
    pass


class SvgOnlyPointerEvents:
    All = "all"

    Painted = "painted"
    Fill = "fill"
    Stroke = "stroke"

    VisiblePainted = "visiblePainted"
    VisibleFill = "visibleFill"
    VisibleStroke = "visibleStroke"
