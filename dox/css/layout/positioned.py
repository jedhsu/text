from ..base import Property


class PositioningDimensions(Dimensions):
    pass


class Position(Property):
    Fixed = "fixed"
    Static = "static"
    Absolute = "absolute"
    Relative = "relative"


class PositionedLayout(Module):
    position: Position

    z_index: Property

    clear: Property
    float: Property
