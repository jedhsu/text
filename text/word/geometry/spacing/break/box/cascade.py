"""

    *Cascade: Break*

"""

from dataclasses import dataclass

from strism._form.cascade import CascadeProperty

__all__ = ["CascadeBreak"]


@dataclass
class CascadeBreak(
    CascadeProperty,
):
    before: type
    after: type
    inside: type
