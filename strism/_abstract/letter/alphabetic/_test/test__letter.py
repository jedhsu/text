"""

    *Abstract Alphabetic Letter,   [Unit Tests]*

"""

from .._letter import Alphabetic
from .._letter import AbstractLetter

from .._letter import AbstractAlphabeticLetter


class TestAbstractAlphabeticLetter:
    def test_init(self):
        lt = AbstractAlphabeticLetter("a")

    def test_invalid_init(self):
        pass
