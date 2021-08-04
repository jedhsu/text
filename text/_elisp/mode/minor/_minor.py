"""

    Minor Mode

"""

from dataclasses import dataclass


from wich.editor.key.map import Keymap

from .._mode import Mode


@dataclass
class MinorMode(
    Mode,
):
    keymap: Keymap
