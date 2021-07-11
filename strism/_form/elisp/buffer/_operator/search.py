from abc import ABCMeta


class Search(
    BufferOperator,
):
    __metaclass__ = ABCMeta


class SearchForward(
    Search,
):
    pass


class SearchBackward(
    Search,
):
    pass
