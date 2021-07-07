from abc import ABCMeta
from dataclasses import dataclass

__all__ = ["AtRule"]


@dataclass
class AtRule:
    __metaclass__ = ABCMeta

    identifier: str

    def into_css(self):
        # [TODO] incomplete
        return "@" + self.identifier


# [TODO] needs refactor, just an organization
class RegularAtRule:
    charset = "charset"
    __import = "import"
    namespace = "namespace"
