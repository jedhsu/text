"""

    *String Whitespacing Protocol*

  The protocol describing treatment of whitespace character for strings.

"""

from .._protocol import StringProtocol

__all__ = ["StringWhitespacingProtocol"]


class StringWhitespacingProtocol(
    StringProtocol,
):
    pass
