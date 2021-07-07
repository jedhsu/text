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
    Block = "block"
    Inline = "inline"
    RunIn = "run-in"


class DisplayInside(Keyword):
    Flow = "flow"
    FlowRoot = "flow-root"

    # [TODO] finish


class DisplayListItem(Keyword):
    ListItem = "list-item"
    # figure this out


class DisplayLegacy(Keyword):
    InlineBlock = "inline-block"
    InlineListItem = "inline-list-item"
    InlineTable = "inline-table"
    InlineFlex = "inline-flex"
    InlineGrid = "inline-grid"


class DisplayBox(Keyword):
    Contents = "contents"
    None_ = "none"


class DisplayInternal(Keyword):
    pass
