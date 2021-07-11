"""

    *Key-Binding*

  A key binding is either a keymap, or a command.

"""

from abc import ABCMeta

__all__ = ["KeyBinding"]


class KeyBinding:
    __metaclass__ = ABCMeta
