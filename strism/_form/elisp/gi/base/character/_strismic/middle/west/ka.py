"""

    *Ka*   ⠅

  The middle-west two key.

"""

from dataclasses import dataclass

from ...._key import CharacterKey
from ...west import WesternKey
from .._key import MiddleKey

__all__ = ["MiddleWestYiki"]


@dataclass
class MiddleWestYiki(
    MiddleKey,
    WesternKey,
    OneKey,
):
    symbol = "\u2805"
