"""

    *Prefix, Bindings*

"""

from ._prefix import Prefix

from .meta import Meta
from .control import Control
from .shift import Shift
from .hyper import Hyper
from .super import Super
from .alt import Alt

__all__ = ["Prefix"]

Prefix.Meta = Meta
Prefix.Control = Control
Prefix.Shift = Shift
Prefix.Hyper = Hyper
Prefix.Super = Super
Prefix.Alt = Alt
