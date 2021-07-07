"""

    *Abstract Element*

  An abstract element is an object.

"""

from abc import ABCMeta

__all__ = ["AbstractElement"]


class AbstractElement:
    __metaclass__ = ABCMeta
