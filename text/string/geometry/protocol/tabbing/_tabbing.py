"""

    *String Tabbing Protocol*

  The protocol describing treatment of tab character for words.

"""

from .._protocol import StringProtocol

__all__ = ["StringWhitespacingProtocol"]


class StringWhitespacingProtocol(
    StringProtocol,
):
    pass
