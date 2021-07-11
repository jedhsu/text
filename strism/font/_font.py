"""

    *Font*

  A font is a mapping from a letter to a glyph.

"""

from typing import Mapping


class Font(
    Mapping[Letter, Glyph],
):
    pass
