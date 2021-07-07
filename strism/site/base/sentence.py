from typing import Sequence

from .decorator import Decorator


class Sentence(str):
    def __init__(
        self,
        sentence: str,
        *decorators: Decorator,
    ):
        self.decorators = {deco.text: deco for deco in decorators}
        super(Sentence, self).__new__(Sentence, sentence)

    decorators: dict[str, Decorator]


# [Test]


class Test:
    sentence = Sentence("I scream for ice cream.", Emphasis("scream", 1))
