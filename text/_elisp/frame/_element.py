"""

    *Frame-Element*

  An element of a frame.

"""

from abc import ABCMeta

from wich.editor._element import Element

__all__ = ["FrameElement"]


class FrameElement(
    Element,
):
    __metaclass__ = ABCMeta
