from dataclasses import dataclass

from . import PseudoClass


root: PseudoClass


@dataclass
class First:
    first: PseudoClass
    first_child: PseudoClass
    # ::first-letter (:first-letter)
    # ::first-line (:first-line)
    first_of_type: PseudoClass


@dataclass
class Last:
    child: PseudoClass
    of_type: PseudoClass


@dataclass
class Nth:
    child: PseudoClass
    col: PseudoClass

    last_child: PseudoClass
    last_col: PseudoClass
    last_of_type: PseudoClass


@dataclass
class Only:
    child: PseudoClass
    of_type: PseudoClass
