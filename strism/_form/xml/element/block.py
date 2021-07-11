from abc import ABCMeta


from .base import Element

class BlockElement(type, Element):

    __metaclass__ = ABCMeta
