from abc import ABCMeta


class Content:
    pass


class Element:
    pass


class Container(type, Element):
    def __prepare__(meta, *args, **kwargs):
        pass

    def into_xml(self):
        pass

    pass
