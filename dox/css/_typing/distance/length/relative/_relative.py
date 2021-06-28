class RelativeUnitLength(
    UnitLength,
):
    pass


class FontRelativeUnit(RelativeUnit):
    cap = "#cap"


class Em(
    RelativeUnitLength,
    Type,
):
    """
    An em is defined as the font size for a given font.

    """

    ident = Ident("em")


class Ex(RelativeUnit):
    """
    Height of a lowercase x.

    """

    symbol = "ex"


class RootEm(RelativeUnit):
    symbol = "rem"


# [TODO] finish


class OneCharacter(
    RelativeUnitLength,
    Type,
):
    pass


class Fraction:
    """
    Fraction unit for grid tracks.

    """

    pass
