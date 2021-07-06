"""

    *Box-Model*

"""

from dataclasses import dataclass

from .content import ContentBox
from .padding import PaddingBox
from .border import BorderBox
from .margin import MarginBox

__all__ = ["BoxModel"]


@dataclass
class BoxModel:
    content: ContentBox
    padding: PaddingBox
    border: BorderBox
    margin: MarginBox
