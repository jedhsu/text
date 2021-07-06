class Minimum(Bound):
    __metaclass__ = ABCMeta


class Minimums:
    width: MinWidth
    height: MinHeight


class MinWidth(
    Property,
    Minimum,
):
    pass


class MinHeight(
    Property,
    Minimum,
):
    pass
