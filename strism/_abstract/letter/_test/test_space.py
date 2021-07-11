from ..space import AbstractLetter

from ..space import AbstractLetterSpace


class TestAbstractLetterSpace:
    def test_init(self):
        space = AbstractLetterSpace(
            "vowels",
            {
                AbstractLetter("a"),
                AbstractLetter("e"),
                AbstractLetter("i"),
                AbstractLetter("o"),
                AbstractLetter("u"),
            },
        )

    def test_create(self):
        pass
