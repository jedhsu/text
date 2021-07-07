"""

    Character-Variant

"""


@dataclass
class CharacterVariant(AtRule):
    character_variant_: Callable
