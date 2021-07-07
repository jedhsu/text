"""

    Cursor Parameters

"""

from typing import Literal
CursorType = Literal["box", "hollow", None, "bar", "bar . width", "hbar", "hbar . height",]

class CursorParameters:
    box: CursorType
    in_non_selected_windows: pass
    x_stretch: pass
    blink_cursor_alist: pass
