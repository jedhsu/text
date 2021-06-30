from dataclasses import dataclass

__all__ = ["InlineElement"]

from .._base import Element


@dataclass
class InlineElement(
    Element,
):
    start: int
    end: int
