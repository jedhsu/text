"""

Multi-column layout.

"""

from dataclasses import dataclass

from ..base import Property


@dataclass
class Column:
    count: Property
    fill: Property
    gap: Property

    span: type
    width: type

    columns: type


@dataclass
class ColumnRule:
    # just a namespace
    column_rule: ShorthandProperty

    color: Property
    style: Property
    width: Property
