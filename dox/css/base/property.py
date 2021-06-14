class Property(str):
    def __init__(self, property: str):
        super(Property, self).__new__(str, property)


class ShorthandProperty(Property):
    pass
