from dataclasses import dataclass

from .texture import StringTexture

__all__ = ["StringGeometry"]


@dataclass
class StringGeometry(
    StringTexture,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        return super(StringGeometry, self,).__init__(
            *args,
            **kwargs,
        )
