from dataclasses import dataclass

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor as InLine


@dataclass
class Syntax(Extension):
    is_xml: bool

    @abstractmethod
    def handleMatch(self):
        pass


class Ellipse(Syntax):
    pass


class Apostrophe(Syntax):
    def handleMatch(self):
        pass

    def extendMarkdown(self):
        pass

    def is_right(self):
        pass


class SmartQuote(Syntax):
    pass


class EmDash(Syntax):
    pass


class NewLine(Syntax):
    pass
