"""

    keyword global

"""

from ._global import GlobalKeyword

from .inherit import InheritKeyword
from .initial import InitialKeyword
from .unset import UnsetKeyword

__all__ = [
    "GlobalKeyword",
    "InheritKeyword",
    "InitialKeyword",
    "UnsetKeyword",
]
