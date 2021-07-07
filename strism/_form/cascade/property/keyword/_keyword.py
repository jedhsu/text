"""

    *CascadeKeyword*

  Usually a value option.

  # [TODO] make rigorous

"""


class CascadeKeyword(
    str,
):
    def __init__(
        self,
        string: str,
    ):
        super(CascadeKeyword, self).__new__(
            str,
            string,
        )


class Test:
    @staticmethod
    def init():
        return CascadeKeyword("abc")
