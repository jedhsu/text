from ..base import Property


class PositioningDimensions(Dimensions):
    pass


class Position(Property):
    Static = "static"

    Fixed = "fixed"
    Absolute = "absolute"
    Relative = "relative"

    def positioned(self) -> bool:
        return True if self == self.Static else False


class PositionedLayout(Module):
    position: Position

    z_index: Property

    clear: Property
    float: Property
