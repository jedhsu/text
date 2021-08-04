"""

    *Frame*

  A frame contains windows.

"""

from wich.editor._element import Element


@dataclass
class Frame(
    Element,
):
    title: FrameTitle
