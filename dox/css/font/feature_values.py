from dataclasses import dataclass
from typing import Callable

from ..base import AtRule


class FontFeatureValues(AtRule):
    swash: AtRule
    annotation: AtRule
    ornaments: AtRule
    stylistic: AtRule
    styleset: AtRule
    character_variant: AtRule


@dataclass
class CharacterVariant(AtRule):
    character_variant_: Callable


@dataclass
class StyleSet(AtRule):
    styleset_: Callable


@dataclass
class Stylistic(AtRule):
    stylistic_: Callable


@dataclass
class AnnotationAt(AtRule):
    annotation_: Callable


@dataclass
class Swash(AtRule):
    swash_: Callable


@dataclass
class Ornaments(AtRule):
    ornaments_: Callable
