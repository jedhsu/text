from ..base import Decorator, Lambda, Symbol, Test


class TestDecorator:
    def test_init(self):
        decorator = Test.adds_period()

        assert isinstance(decorator, Decorator)
        assert isinstance(decorator, Lambda)

        assert decorator.Operand == Symbol("x")
        assert decorator.text == "word"
