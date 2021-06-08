"""

Text utilities.

"""

from typing import Iterable, TypeVar

from returns.pipeline import flow

T = TypeVar("T")


class _Text(str):
    def __init__(self, string: str):
        super(_Text, self).__new__(str, string)


class _Wrap_(_Text):
    def wrap(self, text: str) -> _Text:
        return _Text(f"<{text}>" + self + f"</{text}>")


class _Convert_:
    def into_file_name(self):
        if self == "Title":
            return "index"
        elif self == "Table of Contents":
            return "toc"


class _Pretty_(_Text):
    def pretty(self) -> str:
        return flow(
            self,
            self.replace("à", "&agrave;"),
            self.replace("ï", "&iuml;"),
            self.replace("ø", "&oslash;"),
            self.replace("æ", "&aelig;"),
        )


class _Compute_(_Text):
    @staticmethod
    def max_line_length(
        maxlength: int,
        lines: Iterable[str],
    ):
        for line in lines:
            maxlength = max(maxlength, len(line))
        return maxlength

    @staticmethod
    def pluralize(string: str) -> str:
        return "" if len(string) == 1 else "s"

    def word_count(self) -> int:
        return len(self.split(" "))

    def trim_trailing_newline(self) -> str:
        return self[: len(self) - 1] if self.endswith("\n") else self


class Integer(int):
    def __new__(cls, val: int):
        return super().__new__(int, val)

    def roman(self) -> str:
        if self <= 3:
            return "I" * self
        elif self == 4:
            return "IV"
        elif self <= 10:
            return "V" + "I" * (self - 5)
        else:
            raise ValueError("Value is nota llowed.")

    def with_commas(self) -> str:
        if self > 1000:
            return f"{self // 1000}, {self % 1000}"
        return str(self)


class Text(_Convert_):
    pass
