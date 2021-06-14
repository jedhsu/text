from dataclasses import dataclass


@dataclass
class Break:
    before: type
    after: type
    inside: type


@dataclass
class PageBreak:
    """
    This is deprecated in the language, replaced by Break.

    """

    before: property
    after: property
    inside: property
