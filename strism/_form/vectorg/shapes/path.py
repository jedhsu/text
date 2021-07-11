class Command:
    pass


class Fill(Enum):
    pass


class Color(Enum):
    pass


class Line(Command):
    point: Position
    fill: Fill
    color: Color


class CubicCurve(Command):
    point: Position  # [TODO} should be point
    start_control: Position
    end_control: Position


class Arc(Command):
    pass


class _Into_:
    def into_svg(self) -> str:
        pass


class Path:
    commands: Sequence[Command]
