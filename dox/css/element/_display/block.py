from dataclasses import dataclass


__all__ = ["Block"]

from .._base import Element


@dataclass
class BlockElement(
    Element,
):
    start: property
    end: property


# @dataclass
# class Block:
#     overflow: property
#     size: property
