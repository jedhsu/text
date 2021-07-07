"""

    *Keymap*

  A keymap is a dictionary of key bindings.

"""

from .binding import KeyBinding

__all__ = ["Keymap"]


class Keymap(
    dict,
    KeyBinding,
):
    pass


"""

Action ideas:

Navigate source tree from within buffer.

"""
