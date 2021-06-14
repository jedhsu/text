class FontFamily(str):
    def __init__(self, font: str):
        super(FontFamily, self).__new__(str, font)


class SerifFont(FontFamily, type):
    """
    Font with ligatures.

    """

    pass


class SansSerifFont(type):
    """
    Font without ligatures.

    """

    pass


class MonospaceFont(type):
    """
    Font with fixed-width.

    """

    pass


class CursiveFont(type):
    pass


class FantasyFont(type):
    pass
