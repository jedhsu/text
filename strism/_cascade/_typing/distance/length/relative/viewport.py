__all__ = ["ViewportRelativeLength"]

from ._relative import RelativeUnitLength

from ...._type import Type


class ViewportRelativeUnitLength(
    RelativeUnitLength,
):
    # 1/100th of viewport height
    vh = "#vh"

    # 1/100th of viewport width
    vw = "#vw"

    vmin = "#vmin"
    vmax = "#vmax"


class ViewportWidth(
    ViewportRelativeUnitLength,
    Type,
):
    ident = Ident("vw")


class ViewportHeight(
    ViewportRelativeUnitLength,
    Type,
):
    ident = Ident("vw")


class ViewportMinimumWidth(
    ViewportRelativeUnitLength,
    Type,
):
    ident = Ident("vw")


class ViewportMinimumHeight(
    ViewportRelativeUnitLength,
    Type,
):
    ident = Ident("vw")
