"""

    *Direction-Phantom, Bindings*

"""

from ._class import DirectionPhantom

from .top import TopDirectionPhantom
from .right import RightDirectionPhantom
from .bottom import BottomDirectionPhantom
from .left import LeftDirectionPhantom

__all__ = ["DirectionPhantom"]

DirectionPhantom.Top = TopDirectionPhantom
DirectionPhantom.Right = RightDirectionPhantom
DirectionPhantom.Bottom = BottomDirectionPhantom
DirectionPhantom.Left = LeftDirectionPhantom
