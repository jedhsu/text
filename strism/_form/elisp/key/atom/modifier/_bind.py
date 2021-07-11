"""

    *Modifier-Key, Bindings*

"""

from ._key import ModifierKey

from .meta import Meta
from .control import Control
from .shift import Shift
from .hyper import Hyper
from .super import Super
from .alt import Alt

__all__ = ["ModifierKey"]

ModifierKey.Meta = Meta
ModifierKey.Control = Control
ModifierKey.Shift = Shift
ModifierKey.Hyper = Hyper
ModifierKey.Super = Super
ModifierKey.Alt = Alt
