from dataclasses import dataclass

from ..measure import Length


class WordBreak:
    Normal = "normal"
    BreakAll = "break-all"
    KeepAll = "keep-all"


class WordSpacingKeyword:
    Normal = "normal"


class WordSpacing(WordSpacingKeyword, Length):
    """
    Spacing between each word.

    """

    pass


class WordWrap:
    Normal = "normal"
    BreakWord = "break-word"
    Anywhere = "anywhere"
