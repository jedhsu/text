"""

    *Keyword*

  Usually a value option.

  # [TODO] make rigorous

"""

class Keyword(
    str,
):
    def __init__(
        self,
        string: str,
    ):
        super(Keyword, self).__new__(
            str,
            string,
        )

class Test:
    @staticmethod
    def init():
        return Keyword("abc")
