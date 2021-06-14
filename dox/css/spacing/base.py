from abc import ABCMeta

from ..measure import Length


class Dimensions:
    __metaclass__ = ABCMeta

    top: Length
    right: Length
    bottom: Length
    left: Length
