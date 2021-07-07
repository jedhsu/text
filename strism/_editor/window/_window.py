"""

    *Window*

"""

from dataclasses import dataclass

from wich.editor._element import Element
from wich.editor.frame import Frame
from wich.editor.buffer import Buffer


@dataclass
class Window(
    Element,
):
    parent: Frame
    buffer: dict[Buffer]
    active_buffer: Buffer
    point: WindowPoint
    mark: WindowMark
