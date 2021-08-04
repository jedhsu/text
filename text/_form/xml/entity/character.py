from .base import Entity


class ParameterEntity(Entity):
    pass


class InternalEntity(ParameterEntity):
    pass


class GeneralEntity(Entity):
    pass


class CharacterEntity(GeneralEntity):
    pass


class PredefinedEntity(CharacterEntity):
    pass


class NumberedEntity(CharacterEntity):
    pass


class NamedEntity(CharacterEntity):
    pass


class MixedContentEntity:
    pass
