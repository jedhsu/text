from .._letter import AbstractLetter


class TestAbstractLetter:
    def test_init(self):
        lt = AbstractLetter("a")
        assert isinstance(lt, AbstractLetter)
        assert isinstance(lt, str)
        assert lt == "a"

    def test_invalid_init(self):
        pass
