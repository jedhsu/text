from dataclasses import dataclass


@dataclass
class TextIndent(
    BlockElementOperator,
    Length,
    Percentage,
):
    pass
