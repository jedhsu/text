from dataclasses import dataclass

from ..measure import Length


class WordBreak:
    Normal = "normal"
    BreakAll = "break-all"
    KeepAll = "keep-all"


class WordWrap:
    Normal = "normal"
    BreakWord = "break-word"
    Anywhere = "anywhere"
