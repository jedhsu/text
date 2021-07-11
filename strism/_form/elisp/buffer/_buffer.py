"""

    *Buffer*

  Contains text to be edited.

"""

from abc import ABCMeta
from dataclasses import dataclass

from wich.editor.text import Text

__all__ = ["Buffer"]


@dataclass
class Buffer:
    __metaclass__ = ABCMeta

    # [TODO] this should go in state
    text: Text
    major_mode: MajorMode
