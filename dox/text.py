from typing import Iterable


class _Text(str):
    def __new__(cls, string: str):
        return super().__new__(str, string)


class _Convert_:
    def into_file_name(self):
        if self == "Title":
            return "index"


class _Calculate_(_Text):
    @staticmethod
    def maxlinelength(
        maxlength: int,
        lines: Iterable[str],
    ):
        for line in lines:
            maxlength = max(maxlength, len(line))
        return maxlength


class Int(int):
    def __new__(cls, val: int):
        return super().__new__(int, val)

    def roman():
        pass

    def __repr__():
        pass


class Text(_Convert_):
    pass
