"""

Display property.

Determines how an object is rendered.

"""

from dataclasses import dataclass

from ..base import Property


@dataclass
class Display(Property):
    pass


class DisplayKeyword:
    Block = "block"
    Inline = "inline"
    None_ = "none"
    Contents = "contents"

    Flow = "flow"
    FlowRoot = "flow-root"

    Table = "table"

    # [TODO] finish


"""

Keywords are grouped into six value categories.

"""


class DisplayOutside(Keyword):
    pass


class DisplayInside(Keyword):
    pass


class DisplayListItem(Keyword):
    pass


class DisplayLegacy(Keyword):
    pass


class DisplayBox(Keyword):
    pass


class DisplayInternal(Keyword):
    pass
