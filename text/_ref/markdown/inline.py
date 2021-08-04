from dataclasses import dataclass

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor as InLine


class Inlin


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


@dataclass
class SmartQuote(Syntax):
    is_xml: bool

    def __init__(self, is_xml: bool = False):
        self.is_xml = is_xml
        super(SmartQuote, self).__init__()  # [tODO] fix

    def on_match(parser, match: Match):
        before = -1
        if parser.pos < 0:
            before = parser.char_at(parser.pos - 1)

        # [TODO] finish... boring...


class EmDash(Syntax):
    pass


class NewLine(Syntax):
    pass
